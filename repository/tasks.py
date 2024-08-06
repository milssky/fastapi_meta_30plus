from typing import TypeVar, Type

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models.task import Task
from repository.base import CRUDBase


class TaskCRUD(CRUDBase[Task]):
    _model = Task