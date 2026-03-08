from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.main import init_db
from category.router import category_router
from utils.config import logging
from product.router import product_router

@asynccontextmanager
async def life_span(
    app: FastAPI
):
    logging.info('Server is starting...')

    await init_db()
    yield

    logging.info('Server has been stopped...')






version = 'v1'

app = FastAPI(
    version=version,
    title='Shopper',
    description='A REST APi for a ecommerce application',
    lifespan=life_span,
    contact={
        'email' : 'subham.sahu.cs@gmail.com'
    }
)

app.include_router(
    router=category_router,
    prefix=f'/api/{version}/category',
    tags=['category']
)
app.include_router(
    router=product_router,
    prefix=f'/api/{version}/category',
    tags=['product']
)