
"""
Initialize LEGO app and provide FastAPI object.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .core.database import engine
from .models.base import Base
from .routes.status_check import status_check_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


# FastAPI object creation
app = FastAPI(
    title="LEGO DEV",
    debug=True,
    lifespan=lifespan
)

app.include_router(status_check_router)



