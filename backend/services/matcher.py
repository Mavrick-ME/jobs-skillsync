from sentence_transformers import util
from services.embedder import get_embedding

def match_resume_to_job(resume_text: str, job_text: str) -> float:
    resume_embedding = get_embedding(resume_text)
    job_embedding = get_embedding(job_text)
    score = util.cos_sim(resume_embedding, job_embedding)
    return round(float(score[0][0]), 4)