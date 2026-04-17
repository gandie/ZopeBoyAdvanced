# file: my_fastapi_app.py
from fastapi import FastAPI

asgi_app = FastAPI()

@asgi_app.get("/hello")
def hello():
    return {"message": "Hello from ASGI!"}
