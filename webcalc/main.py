from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import RedirectResponse


class Item(BaseModel):
    a: int
    b: int


app = FastAPI()


@app.get("/", include_in_schema=False)
async def redirect():
    response = RedirectResponse(url='/docs')
    return response


@app.post("/sum")
async def root(arg: Item) -> int:
    return arg.a+arg.b


@app.post("/mult")
async def root(arg: Item) -> int:
    return 42
