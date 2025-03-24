from fastapi import APIRouter, Depends

from main.core.database import get_db_session
from main.services.get_lego_parts import get_records
from sqlalchemy.orm import Session

status_check_router = APIRouter()




@status_check_router.get("/")
def welcome():
    return {"response": "OK"}

@status_check_router.get("/check_db")
def check_db(db_session: Session = Depends(get_db_session)):
    records = get_records(db_session) 
    return {"response": records}
