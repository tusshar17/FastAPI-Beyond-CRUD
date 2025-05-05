from pydantic import BaseModel
from datetime import datetime
import uuid


class Book(BaseModel):
    uid: uuid.UUID
    title: str
    author: str
    published_date: int
    created_at: datetime
    updated_at: datetime


class BookCreateModel(BaseModel):
    title: str
    author: str
    published_date: int


class BookUpdateModel(BaseModel):
    title: str
    author: str
    published_date: int


class BookDetailModel(Book):
    pass
