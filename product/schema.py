from pydantic import BaseModel
import uuid




class ProductResponse(BaseModel):
    __tablename__ = 'product'
    uid: uuid.UUID 
    title: str 
    description: str
    image: str|None 
    price: float 
    categoryId: uuid.UUID 