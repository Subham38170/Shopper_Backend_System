from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from db.models.category import Category
from fastapi import HTTPException,status

class CategoryService:
    async def get_categories(
        self,
        session: AsyncSession
    ):
        try:
            statement = select(Category)
            result = await session.exec(statement)
            
            
            return result.all()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=str(e)
            )