from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Schema
class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    in_stock:bool

@app.get('/')
def index():
    return {"message":"Hello World"}

# Greeting (localhost:8000/greet/Max)
@app.get('/greet/{name}')
def greet_name(name:str):
    return {"greeting":f"Hello {name}"}


# Query string greeting (localhost:8000/greet?name=Max)
@app.get('/greet')
def greet_optional_name(name:Optional[str] = "user"):
    return {"message_user":f"Hello {name}"}


# Item Updates (localhost:8000/item/1)
@app.put('/item/{item_id}')
def update_item(item_id:int, item:Item):
    return {'name':item.name,
            'description':item.description,
            'price':item.price,
            'in_stock':item.in_stock
            }