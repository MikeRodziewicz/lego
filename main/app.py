
"""
Initialize LEGO app and provide FastAPI object.
"""

from fastapi import FastAPI
from sqlalchemy.orm import Session

from .models.parts import Base, LegoPart

from .db.database import SessionLocal, engine


Base.metadata.create_all(bind=engine)


app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"response": "OK"}



