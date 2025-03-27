from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_date: int


class BookUpdateModel(BaseModel):
    title: str
    author: str
    published_date: int