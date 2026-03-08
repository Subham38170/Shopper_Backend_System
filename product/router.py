from fastapi import APIRouter,Depends
from .schema import ProductResponse
from .schema import ProductResponse
from .services import Productservice
from sqlmodel.ext.asyncio.session import AsyncSession
from db.main import get_session


product_router = APIRouter()


product_service = Productservice()

@product_router.get('/',response_model=ProductResponse)
async def get_categories(
    session: AsyncSession = Depends(get_session)
): 
    response = await product_service.get_products(session)

    return response
