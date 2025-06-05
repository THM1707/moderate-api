from fastapi import FastAPI, Query, Form
from pydantic import BaseModel, Field
from typing import Annotated


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class FormData(BaseModel):
    username: str = Field(..., max_length=3)
    password: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# Request body example
@app.post("/items/")
async def create_item(item: Item):
    # FastAPI will directly parse the JSON in request body
    return item


@app.get("/items/")
async def read_items(q: Annotated[str | None, Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Query parameter example
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # todo: find out how to customize the default error response
    return {"item_id": item_id}


@app.post("/login/")
async def login(data: Annotated[FormData, Form()]):
    return data
