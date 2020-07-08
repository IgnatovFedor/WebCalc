from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    a: int
    b: int


app = FastAPI()


@app.post("/sum")
async def root(arg: Item) -> int:
    return arg.a+arg.b


@app.post("/mult")
async def root(arg: Item) -> int:
    return 42
