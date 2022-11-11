from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Optional
app = FastAPI()
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item():
    def __init__(self, title: str, value: int):
        self.title = title
        self.value = value
        self.id = len(items) + 1


class ItemModel(BaseModel):
    title: str
    value: int


items: list[Item] = []


@app.get('/')
def index():
    return {'data': {"items": items}}


@app.post('/')
def index(item: ItemModel) -> Item:
    _item = Item(item.title, item.value)
    items.append(_item)
    return {'data': {"item": _item}}
