# from sqlalchemy import Column, Integer, String
# from . database import Base

# class Notes(Base):
#     __tablename__ = 'notes'

#     id = Column(Integer, Primary_key = True, index = True)
#     title = Column(String)
#     content = Column(String)

from sqlalchemy import Table, Column, Integer, String
from .database import metadata

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("title", String, index=True),
    Column("content", String),
)