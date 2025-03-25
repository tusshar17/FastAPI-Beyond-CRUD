from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
async def read_root():
    return {
        'messsage': 'Hello World!'
    }


# using path parameter
@app.get('/greet/{name}')
async def greet_name(name: str) -> dict:
    return {
        'message': f'Hello {name}!'
    }


# using query parameter
@app.get('/say-hello')
async def say_hello(name: str) -> dict:
    return {
        'message': f'Hello {name}!'
    }


# using optional query parameter
@app.get('/greet')
async def greet_user(name: Optional[str] = 'User', age: int = 0) -> dict:
    return {
        'message': f'Hello {name}!',
        'age': age
    }


# handling headers
@app.get('/get-headers')
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
):
    request_headers = {}

    request_headers['Accept'] = accept
    request_headers['Content-Type'] = content_type
    request_headers['User-Agent'] = user_agent
    request_headers['Host'] = host

    return request_headers


# ===== CRUD Operations ===== 
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "published_date": 1960},
    {"id": 2, "title": "1984", "author": "George Orwell", "published_date": 1949},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "published_date": 1813},
    {"id": 4, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_date": 1925},
    {"id": 5, "title": "Moby-Dick", "author": "Herman Melville", "published_date": 1851},
    {"id": 6, "title": "War and Peace", "author": "Leo Tolstoy", "published_date": 1869},
    {"id": 7, "title": "The Catcher in the Rye", "author": "J.D. Salinger", "published_date": 1951},
    {"id": 8, "title": "The Hobbit", "author": "J.R.R. Tolkien", "published_date": 1937},
    {"id": 9, "title": "Brave New World", "author": "Aldous Huxley", "published_date": 1932},
    {"id": 10, "title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "published_date": 1866}
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    published_date: int


class BookUpdateModel(BaseModel):
    title: str
    author: str
    published_date: int

@app.get('/books', response_model=List[Book])
async def get_all_books():
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/book/{book_id}')
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')

@app.patch('/book/{book_id}')
async def update_book(book_id: int, book_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_data.title
            book['published_date'] = book_data.published_date
            book['author'] = book_data.author
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')

@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Book not found')
