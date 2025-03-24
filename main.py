from fastapi import FastAPI, Header
from typing import Optional
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


# schema to create a book
class BookCreateModel(BaseModel):
    title: str
    author: str

# create book using rquest body
@app.post('/create-book')
async def create_book(book_data: BookCreateModel):
    return {
        'book_data': book_data
    }