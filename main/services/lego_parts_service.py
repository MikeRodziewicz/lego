
from sqlalchemy.orm import Session

from main.dto_schemas.lego_part_dto import LegoPartDTO
from main.exceptions.db_exceptions import NoRecordFoundDBException
from main.models.parts import LegoPart


def get_records(db_session: Session) -> list:
    records = db_session.query(LegoPart).all()
    if not len(records):
        raise NoRecordFoundDBException()
    return records

def insert_record(db_session: Session, lego_part: LegoPartDTO) -> None:
    part = LegoPart(**lego_part)
    db_session.add(part)
