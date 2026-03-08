from sqlmodel import SQLModel, Column,Field,Relationship
from .category import Category
import uuid
import sqlalchemy.dialects.postgresql as pg

class Product(SQLModel,table=True):
    __tablename__ = 'product'
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    title: str = Field(min_length=4)
    description: str = Field(min_length=12)
    image: str|None = Field(default=None)
    price: float = Field(default='0.0')
    categoryId: uuid.UUID = Field(foreign_key='category.uid')

    category: Category = Relationship(back_populates='categories')