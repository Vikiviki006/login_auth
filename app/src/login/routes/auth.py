# app/routes/auth.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.src.login.schemas import UserCreate, UserLogin
from app.src.login.controller import create_user, authenticate_user

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    new_user = create_user(db, user.email, user.password)
    return {"id": new_user.id, "email": new_user.email}

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    token = authenticate_user(db, user.email, user.password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"access_token": token, "token_type": "bearer"}