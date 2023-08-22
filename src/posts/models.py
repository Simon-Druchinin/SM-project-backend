from datetime import datetime

from sqlalchemy import TIMESTAMP, Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from src.database import Base
from src.auth.models import User


class Statistics():
    views: Mapped[int] = mapped_column(Integer, default=0)
    likes: Mapped[int] = mapped_column(Integer, default=0)

class Post(Base, Statistics):
    __tablename__ = 'posts_posts'
    
    id: int = Column(Integer, primary_key=True, index=True)
    author_id: str = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    text: str = Column(String, nullable=False)
    title: str = Column(String(255), nullable=False)
    created_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)
    
    author = relationship(User, back_populates="posts")

class Comment(Base, Statistics):
    __tablename__ = 'posts_comments'
    
    id: int = Column(Integer, primary_key=True, index=True)
    author_id: str = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    created_at: datetime = Column(TIMESTAMP, default=datetime.utcnow)
    
    author = relationship(User, back_populates="comments")