from pydantic import BaseModel, ConfigDict

class Item(BaseModel):
    id:int
    name:str
    description:str
    price:int
    in_stock:bool

    # Allows Pydantic to read directly from object attributes (SQLAlchemy uses ORM objects)
    model_config = ConfigDict(from_attributes=True)