
"""
Initialize LEGO app and provide FastAPI object.
"""

from fastapi import FastAPI

from .core.database import engine
from .models.base import Base 
from .routes.status_check import status_check_router


# DB models setup phase
Base.metadata.create_all(bind=engine)


# FastAPI object creation
app = FastAPI(
    title="LEGO DEV",
    debug=True,
)

app.include_router(status_check_router)



