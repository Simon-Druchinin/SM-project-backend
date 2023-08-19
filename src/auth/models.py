from datetime import datetime
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Boolean, MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, JSON, Column
from sqlalchemy import TIMESTAMP, Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


metadata = MetaData()

class Role(Base):
    __tablename__ = 'auth_roles'
    metadata = metadata

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255))
    permissions: Mapped[str] = mapped_column(JSON)

class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = 'auth_users'
    metadata = metadata

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    username: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=datetime.utcnow)
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey(Role.id))
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
