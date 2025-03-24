from fastapi import FastAPI
from typing import Optional

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