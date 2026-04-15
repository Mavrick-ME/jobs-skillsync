from fastapi import APIRouter, UploadFile, File, Form
from typing import List
import tempfile, os, shutil
from services.parser import parse_resume
from services.ranker import rank_candidates

router = APIRouter()

@router.post("/rank")
async def rank_resumes(
    job_title: str = Form(...),
    job_description: str = Form(...),
    resumes: List[UploadFile] = File(...)
):
    parsed_resumes = []

    for resume_file in resumes:
        # Save uploaded file temporarily
        suffix = os.path.splitext(resume_file.filename)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(resume_file.file, tmp)
            tmp_path = tmp.name

        # Parse the resume text
        text = parse_resume(tmp_path)
        os.unlink(tmp_path)  # delete temp file

        name = os.path.splitext(resume_file.filename)[0]
        parsed_resumes.append({
            "name": name,
            "file_name": resume_file.filename,
            "text": text
        })

    # Rank all resumes against the job description
    results = rank_candidates(parsed_resumes, job_description)
    return results