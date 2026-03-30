# app/utils/security.py

from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

SECRET_KEY = "secret"
ALGORITHM = "HS256"

def hash_password(password: str):
    password = password[:72] 
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    plain = plain[:72]
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    data.update({"exp": datetime.utcnow() + timedelta(hours=1)})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)