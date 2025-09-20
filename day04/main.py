from fastapi import FastAPI, status, HTTPException, Query
from decimal import Decimal
from fastapi.encoders import jsonable_encoder
from typing import Optional
from pydantic import BaseModel, Field, condecimal

class ItemIn(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    price: condecimal(gt=0, max_digits=10, decimal_places=2)
    tags: list[str] = []

class ItemOut(ItemIn):
    id: int

items: list[ItemOut] = []


app = FastAPI()

# POST /items
@app.post("/items", status_code=status.HTTP_201_CREATED,
          response_model=ItemOut)
def create_item(item: ItemIn):
    new_id = len(items) + 1
    item_out = ItemOut(id=new_id, **item.model_dump())
    items.append(item_out)
    return jsonable_encoder(item_out)

# GET /items/{item_id}
@app.get("/items/{item_id}", response_model=ItemOut)
def read_item(item_id: int):
    for itm in items:
        if itm.id == item_id:
            return itm
    raise HTTPException(status_code=404, detail="Item not found")

# GET /items
@app.get("/items", response_model=list[ItemOut])
def list_items(
    min_price: float | None = Query(None, gt=0),
    tag: str | None = None,
):
    data = items
    if min_price is not None:
        data = [i for i in data if i.price >= min_price]
    if tag is not None:
        data = [i for i in data if tag in i.tags]
    return data
    