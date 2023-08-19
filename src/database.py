from typing import AsyncGenerator
from sqlalchemy import MetaData

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from src.config import config

DATABASE_URL = f"postgresql+asyncpg://{config.db.USER}:{config.db.PASSWORD}@{config.db.HOST}:{config.db.PORT}/{config.db.NAME}"

class Base(DeclarativeBase):
    pass


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
    