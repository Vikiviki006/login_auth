# main.py

from fastapi import FastAPI
from app.src.login.routes import auth, user
from app.config.database import init_db

app = FastAPI()


@app.on_event("startup")
def startup_event():
    init_db()


app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/users")