from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.models import get_db, Job, MatchResult

router = APIRouter()

@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total_jobs = db.query(Job).count()
    total_resumes = db.query(MatchResult).count()
    strong_matches = db.query(MatchResult).filter(
        MatchResult.status == "Strong Match"
    ).count()

    return {
        "total_jobs": total_jobs,
        "total_resumes": total_resumes,
        "strong_matches": strong_matches
    }


@router.delete("/job/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db)):
    db.query(MatchResult).filter(MatchResult.job_id == job_id).delete()
    db.query(Job).filter(Job.id == job_id).delete()
    db.commit()
    return {"message": "Job deleted successfully"}


@router.delete("/reset")
def reset_all(db: Session = Depends(get_db)):
    db.query(MatchResult).delete()
    db.query(Job).delete()
    db.commit()
    return {"message": "System reset successfully"}