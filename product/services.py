from db.models.product import Product
from utils.config import logging
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession



class Productservice:
    async def get_products(
        self,
        session: AsyncSession
    ):
        try:
            products = select(Product)
            result = await session.exec(products)
            return result.all()
        except Exception as e:
            logging.info(str(e))
            raise Exception(e)


        