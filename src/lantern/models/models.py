from sqlalchemy import MetaData, Table, Column, Integer, String
metadata = MetaData()

flashlights = Table(
    "flashlights",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("status", String, nullable=False),
    Column("color", String, nullable=False),
)
