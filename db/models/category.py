from sqlmodel import SQLModel,Field,Column,Relationship
import sqlalchemy.dialects.postgresql as pg
import uuid
from typing import List



class Category(SQLModel,table=True):
    __tablename__ = 'category'
    uid: uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            nullable=False,
            primary_key=True,
            default=uuid.uuid4
        )
    )
    title: str
    image: str|None = Field(default=None)

    product: List['Product'] = Relationship(back_populates='category')