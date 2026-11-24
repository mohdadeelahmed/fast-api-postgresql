from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import Optional, List
from database import SessionLocal
import models

app = FastAPI()

# Schema
class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    in_stock:bool

class Config:
    orm_model = True


db=SessionLocal()

# Implement CRUD routes using database

@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items():
    items = db.query(models.Item).all()

    return items


@app.get('/item/{item_id}')
def get_an_item(item_id:int):  # note: Pydantic uses typehinting
    pass


@app.post('/items', response_model=Item, status_code=201)
def create_an_item(item:Item):
    new_item = models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        in_stock=item.in_stock
    )

    db.add(new_item)
    db.commit()

    return new_item


@app.put('/item/{item_id}')
def update_an_item(item_id:int):
    pass


@app.delete('/item/{item_id}')
def delete_an_item(item_id:int):
    pass
