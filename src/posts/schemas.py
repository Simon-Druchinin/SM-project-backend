from datetime import datetime
from pydantic import BaseModel

from src.auth.schemas import UserGeneralReadSchema


class PostReadSchema(BaseModel):
    id: int
    title: str
    text: str
    created_at: datetime
    views: int
    likes: int
    author: UserGeneralReadSchema

class PostCreateSchema(BaseModel):
    title: str
    text: str
    author_id: int
