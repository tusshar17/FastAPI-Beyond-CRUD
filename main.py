from fastapi import FastAPI, Header
from typing import Optional
from src.books.routes import book_router

version = 'v1'

app = FastAPI(
    version = version
)


app.include_router(book_router, prefix=f'/api/{version}/books')


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