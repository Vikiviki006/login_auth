# app/services/auth_service.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.user import User
from app.src.utils.security import hash_password, verify_password, create_token

def create_user(db: Session, email: str, password: str):
    existing = db.query(User).filter(User.email == email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()

    if not user or not verify_password(password, user.password):
        return None

    token = create_token({"user_id": user.id})
    return token