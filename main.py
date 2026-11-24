from fastapi import FastAPI, status, HTTPException
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


@app.get('/item/{item_id}', response_model=Item, status_code=200)
def get_an_item(item_id:int):  # note: Pydantic uses typehinting
    item = db.query(models.Item).filter(models.Item.id==item_id).first()

    return item


@app.post('/items', response_model=Item, status_code=201)
def create_an_item(item:Item):

    # Duplicate items check
    db_item = db.query(models.Item).filter(models.Item.name==item.name).first()

    if db_item is not None:
        raise HTTPException(status_code=400, detail="Item already exists")

    new_item = models.Item(
        name=item.name,
        price=item.price,
        description=item.description,
        in_stock=item.in_stock
    )

    db.add(new_item)
    db.commit()

    return new_item


@app.put('/item/{item_id}', response_model=Item, status_code=200)
def update_an_item(item_id:int, item:Item):
    updated_item = db.query(models.Item).filter(models.Item.id==item_id).first()

    updated_item.name = item.name
    updated_item.price = item.price
    updated_item.description = item.description
    updated_item.in_stock = item.in_stock

    db.commit()

    return updated_item


@app.delete('/item/{item_id}')
def delete_an_item(item_id:int):
    deleted_item = db.query(models.Item).filter(models.Item.id==item_id).first()

    if deleted_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(deleted_item)
    db.commit()

    return deleted_item