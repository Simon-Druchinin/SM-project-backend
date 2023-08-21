from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis

from src.auth.config import auth_backend, fastapi_users
from src.auth.schemas import UserRead, UserCreate

from src.menu.router import router as menu_router
from src.tasks.router import router as tasks_router

from src.config import config

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
app.include_router(tasks_router)

@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url(f"redis://{config.redis.HOST}:{config.redis.PORT}", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
