from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.routers import router
from core.config import settings
from core.db import create_db_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_tables()
    yield


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    lifespan=lifespan
)

app.include_router(router=router)
