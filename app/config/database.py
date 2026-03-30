# app/config/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:viki2006@localhost/login"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def init_db():
    # import all modules here to ensure models are registered on Base.metadata
    from app.models import user  # noqa: F401
    Base.metadata.create_all(bind=engine)