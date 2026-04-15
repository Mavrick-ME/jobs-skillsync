from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def jobs_home():
    return {"message": "Jobs routes working"}