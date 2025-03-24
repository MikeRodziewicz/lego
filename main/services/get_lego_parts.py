

from sqlalchemy.orm import Session

from main.models.parts import LegoPart


def get_records(db_session: Session):
    records = db_session.query(LegoPart).all()
    return records

