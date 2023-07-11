import enum
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Enum

Base = declarative_base()


class Meaning(enum.Enum):
    one = "Включён"
    two = "Выключен"


class Colors(enum.Enum):
    yellow = "Жёлтый"
    white = "Белый"
    black = "Чёрный"
    green = "Зелёный"
    red = "Красный"
    blue = "Синий"


class Lantern(Base):
    __tablename__ = 'lantern'

    id = sa.Column(sa.Integer, primary_key=True)
    status = sa.Column(sa.Enum(Meaning))
    color = sa.Column(sa.Enum(Colors))

