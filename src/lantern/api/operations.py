from typing import List

from fastapi import APIRouter, HTTPException
from fastapi import Depends
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .. import table
from ..database import get_session
from ..models.operations import Operation

router = APIRouter(
    prefix='/operations',
)


flashlights = [
    {"id": 1, "status": "Включен", "color": "Белый"},
    {"id": 2, "status": "Выключен", "color": "Чёрный"}
]


@router.get("/lantern")
def get_lantern():
    return flashlights


class Flashlight(BaseModel):
    status: str
    color: str


@router.put("/flashlight/{flashlight_id}", response_model=Flashlight)
def update_lanterns(flashlight_id: int, data: Flashlight):
    for item in flashlights:
        if item['id'] == flashlight_id:
            item.update(data.dict())
            return item
    raise HTTPException(status_code=404, detail="Item not found")

