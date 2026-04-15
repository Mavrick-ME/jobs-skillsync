from sentence_transformers import util
from backend.services.embedder import get_embedding

def match_resume_to_job(resume_text: str, job_text: str) -> float:
    """
    Returns a similarity score between 0 and 1.
    0 = no match, 1 = perfect match
    """
    resume_embedding = get_embedding(resume_text)
    job_embedding = get_embedding(job_text)
    score = util.cos_sim(resume_embedding, job_embedding)
    return round(float(score[0][0]), 4)