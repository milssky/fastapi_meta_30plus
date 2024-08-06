from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_session
from repository.tasks import TaskCRUD
from schemas.task import TaskWrite


task_router = APIRouter()


@task_router.post("/tasks")
async def get_tasks(
    task: TaskWrite,
    session: AsyncSession = Depends(get_session)
):
    return await TaskCRUD.create(session, task)
