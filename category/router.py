from fastapi import APIRouter,Depends
from db.main import get_session
from sqlmodel.ext.asyncio.session import AsyncSession
from .services import CategoryService
from .schema import Category
category_router = APIRouter()

category_service = CategoryService()

@category_router.get('/',response_model=Category)
async def get_categories(
    session: AsyncSession = Depends(get_session)
): 
    response = await category_service.get_categories(session)

    return response
