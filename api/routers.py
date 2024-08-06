from fastapi import APIRouter

from api.endpoints.task import task_router


router = APIRouter()
router.include_router(
    task_router,
    prefix='',
    tags=['tags']
)