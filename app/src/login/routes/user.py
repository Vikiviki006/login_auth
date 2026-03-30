from fastapi import APIRouter, Depends
from app.middleware.auth_middleware import get_current_user

router = APIRouter()

@router.get("/profile")
def profile(user=Depends(get_current_user)):
    return {"id": user.id, "email": user.email}