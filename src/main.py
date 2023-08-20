from fastapi import FastAPI

from src.auth.config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.menu.router import router as menu_router

app = FastAPI(
    title="My app"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(menu_router)
