import sys
sys.path.insert(0, "backend")

from services.matcher import match_resume_to_job

def test_high_similarity():
    resume = "Python developer with FastAPI, machine learning and NLP experience"
    job = "Looking for Python developer with FastAPI and machine learning skills"
    score = match_resume_to_job(resume, job)
    assert score > 0.5
    print(f"✅ High similarity test passed! Score: {score}")

def test_low_similarity():
    resume = "Graphic designer with Photoshop and Illustrator skills"
    job = "Looking for Python developer with machine learning experience"
    score = match_resume_to_job(resume, job)
    assert score < 0.6
    print(f"✅ Low similarity test passed! Score: {score}")

def test_score_range():
    resume = "Data scientist with Python and TensorFlow"
    job = "ML engineer with deep learning experience"
    score = match_resume_to_job(resume, job)
    assert 0.0 <= score <= 1.0
    print(f"✅ Score range test passed! Score: {score}")