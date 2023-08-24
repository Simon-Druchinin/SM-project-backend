from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.posts.models import posts

from src.database import get_async_session


async def post_exists(post_id: int, session: AsyncSession) -> bool:
    result = await session.execute(select(exists().where(posts.c.id == post_id)))

    return result.all()[0][0]

