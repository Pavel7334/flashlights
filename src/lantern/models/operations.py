from pydantic import BaseModel


class Operation(BaseModel):
    id: int
    status: str
    color: str

    class Config:
        orm_mode = True
