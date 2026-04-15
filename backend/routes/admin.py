from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def admin_home():
    return {"message": "Admin routes working"}