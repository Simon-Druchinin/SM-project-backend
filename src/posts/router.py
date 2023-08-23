from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import User
from src.database import get_async_session
from src.posts.models import Post
from src.posts.schemas import PostReadSchema
from src.auth.schemas import UserGeneralReadSchema

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

posts = Post.__table__
users = User.__table__

@router.get("/")
async def get_posts(session: AsyncSession = Depends(get_async_session)) -> list[PostReadSchema]:
    query = select(posts, users).where(posts.c.author_id == users.c.id).order_by(posts.c.created_at.desc())
    result = await session.execute(query)
    result = [
        PostReadSchema(
            id=post.id,
            title = post.title,
            text = post.text,
            created_at = post.created_at,
            views = post.views,
            likes = post.likes,
            author = UserGeneralReadSchema(
                id = post.author_id,
                email = post.email,
                username = post.username,
            )
        )
        for post in result.all()
    ]

    return result
