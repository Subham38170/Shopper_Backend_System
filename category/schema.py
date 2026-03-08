from pydantic import BaseModel,Field
from uuid import UUID


class Category(BaseModel): 
    uid: UUID
    title: str
    image: str|None = Field(default=None)