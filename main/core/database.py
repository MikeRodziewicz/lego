"""
Main module for database configuration and setup.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


DATABASE_URL = "sqlite:///./lego.db"
engine = create_engine(DATABASE_URL)

def get_db_session(): 
    with Session(bind=engine) as session:
        yield session
