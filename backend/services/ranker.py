from services.matcher import match_resume_to_job

def rank_candidates(resumes: list, job_description: str) -> list:
    results = []
    for resume in resumes:
        score = match_resume_to_job(resume["text"], job_description)
        results.append({
            "name": resume["name"],
            "file_name": resume["file_name"],
            "score": score,
            "match_percentage": f"{round(score * 100, 1)}%",
            "status": get_status(score)
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results

def get_status(score: float) -> str:
    if score >= 0.85:
        return "Strong Match"
    elif score >= 0.5:
        return "Moderate Match"
    else:
        return "Poor Fit"