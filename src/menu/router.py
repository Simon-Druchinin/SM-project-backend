from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.menu.models import HeaderMenu
from src.menu.schemas import HeaderMenuReadCreateSchema

router = APIRouter(
    prefix="/menu",
        tags=["Menu"]
    )

@router.get("/")
async def get_header_menu(session: AsyncSession = Depends(get_async_session)) -> list[HeaderMenuReadCreateSchema]:
    query = select(HeaderMenu.__table__)
    result = await session.execute(query)
    return result.all()

@router.post("/")
async def add_header_menu(new_header_menu: HeaderMenuReadCreateSchema, session: AsyncSession = Depends(get_async_session)):
    statement = insert(HeaderMenu).values(**new_header_menu.model_dump())
    await session.execute(statement)
    await session.commit()
    return {"result": "success"}
