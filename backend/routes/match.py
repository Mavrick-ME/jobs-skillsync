from services.bias_filter import apply_bias_filter, get_anonymized_name
from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from typing import List
import tempfile, os, shutil
from services.parser import parse_resume
from services.ranker import rank_candidates
from services.extractor import extract_info
from database.models import get_db, Job, MatchResult

router = APIRouter()

@router.post("/rank")
async def rank_resumes(
    job_title: str = Form(...),
    job_description: str = Form(...),
    resumes: List[UploadFile] = File(...),
    db: Session = Depends(get_db)
):
    parsed_resumes = []

    for resume_file in resumes:
        suffix = os.path.splitext(resume_file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(resume_file.file, tmp)
            tmp_path = tmp.name

        # Parse text
        text = parse_resume(tmp_path)
        os.unlink(tmp_path)

        # Apply bias filter BEFORE extracting info
        filtered_text = apply_bias_filter(text)

        # Extract skills using NER on filtered text
        info = extract_info(filtered_text)

        name = os.path.splitext(resume_file.filename)[0]
        parsed_resumes.append({
            "name": info["name"] if info["name"] != "Unknown" else name,
            "file_name": resume_file.filename,
            "text": filtered_text,
            "skills": info["skills"],
            "skill_count": info["skill_count"]
        })

    # Rank candidates
    results = rank_candidates(parsed_resumes, job_description)

    # Save job to database
    strong_count = sum(1 for r in results if r["status"] == "Strong Match")
    job = Job(
        title=job_title,
        description=job_description,
        total_candidates=len(results),
        strong_matches=strong_count
    )
    db.add(job)
    db.commit()
    db.refresh(job)

    # Save each result
    for r in results:
        match = MatchResult(
            job_id=job.id,
            candidate_name=r["name"],
            file_name=r["file_name"],
            score=r["score"],
            match_percentage=r["match_percentage"],
            status=r["status"]
        )
        db.add(match)
    db.commit()

    return {"job_id": job.id, "results": results}


@router.get("/history")
def get_history(db: Session = Depends(get_db)):
    jobs = db.query(Job).order_by(Job.created_at.desc()).all()
    return [
        {
            "id": j.id,
            "title": j.title,
            "date": j.created_at.strftime("%d %b %Y"),
            "total_candidates": j.total_candidates,
            "strong_matches": j.strong_matches
        }
        for j in jobs
    ]


@router.get("/history/{job_id}")
def get_job_results(job_id: int, db: Session = Depends(get_db)):
    job = db.query(Job).filter(Job.id == job_id).first()
    results = db.query(MatchResult).filter(MatchResult.job_id == job_id).all()
    return {
        "job_id": job_id,
        "title": job.title,
        "results": [
            {
                "name": r.candidate_name,
                "file_name": r.file_name,
                "score": r.score,
                "match_percentage": r.match_percentage,
                "status": r.status
            }
            for r in results
        ]
    }