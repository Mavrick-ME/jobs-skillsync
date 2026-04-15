from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def resume_home():
    return {"message": "Resume routes working"}