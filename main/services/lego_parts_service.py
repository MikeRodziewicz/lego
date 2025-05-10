
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
    prt_one = LegoPartDTO.model_dump(lego_part)
    print(prt_one)
    part = LegoPart(**prt_one)
    print(part)
    db_session.add(part)
    db_session.commit()
