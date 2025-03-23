"""
Basic part models.
"""

from sqlalchemy import Column, Integer, String

from main.db.database import Base


class LegoPart(Base):
    """ Base LEGO part model"""

    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True)
    lego_id = Column(Integer, nullable=False)
    part_name = Column(String)

