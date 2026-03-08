from utils.config import Settings
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from sqlalchemy.orm import sessionmaker



Config = Settings()

engine = create_async_engine(
    url=Config.DATABASE_URL,
    echo = True
)
    
async def init_db():
    async with engine.begin() as conn:

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():
    Session = sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=AsyncSession
    )

    async with Session() as session:
        yield session
