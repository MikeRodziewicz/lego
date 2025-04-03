from pydantic import BaseModel


class LegoPartDTO(BaseModel):
    lego_id: int
    part_name: str
