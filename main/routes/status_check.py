from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import except_
from sqlalchemy.orm import Session

from main.core.database import get_db_session
from main.dto_schemas.lego_part_dto import LegoPartDTO
from main.exceptions.db_exceptions import NoRecordFoundDBException
from main.services.lego_parts_service import get_records, insert_record

status_check_router = APIRouter()




@status_check_router.get("/")
def welcome():
    return {"response": "OK"}

@status_check_router.get("/check_db")
def check_db_get(db_session: Session = Depends(get_db_session)):
    try:
        records = get_records(db_session) 
    except NoRecordFoundDBException as e:
        raise HTTPException(404,detail=e._default_msg)
    return {"response": records}


@status_check_router.post("/check_db")
def check_db_insert(part: LegoPartDTO ,db_session: Session = Depends(get_db_session)):
    try:
        records = insert_record(db_session, part) 
    except NoRecordFoundDBException as e:
        raise HTTPException(404,detail=e._default_msg)
    return {"response": records}


