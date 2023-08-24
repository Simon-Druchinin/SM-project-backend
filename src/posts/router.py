from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession


from src.auth.models import User
from src.auth.schemas import UserGeneralReadSchema
from src.auth.config import current_user

from src.database import get_async_session

from src.posts.models import posts
from src.posts.utils import post_exists
from src.posts.schemas import PostReadSchema, PostCreateSchema


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

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

    return {
        "status": status.HTTP_200_OK,
        "data": result,
        "detail": None
    }

@router.get("/{post_id}")
async def get_post(post_id: int, session: AsyncSession = Depends(get_async_session)):
    if not await post_exists(post_id, session):
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "msg": "Post with such id was not found"
            }
        )

    query = select(posts, users).where(posts.c.id == post_id)
    result = await session.execute(query)

    post = result.all()[0]

    post = PostReadSchema(
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

    return {
        "status": status.HTTP_200_OK,
        "data": post,
        "detail": None
    }



@router.post("/")
async def create_post(new_post: PostCreateSchema, current_user: User = Depends(current_user), session: AsyncSession = Depends(get_async_session)):
    statement = insert(posts).values(**new_post.model_dump()).returning(posts.c.id)
    result = await session.execute(statement)
    await session.commit()

    return {
        "status": status.HTTP_201_CREATED,
        "data": result,
        "detail": None
    }

