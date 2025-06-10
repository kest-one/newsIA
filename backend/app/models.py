from typing import Optional
from sqlmodel import SQLModel, Field


class Source(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    source_id: Optional[int] = Field(default=None, foreign_key="source.id")


class Feedback(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    item_id: int = Field(foreign_key="item.id")
    rating: int
    comment: Optional[str] = None
