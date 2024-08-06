from typing import Generic, TypeVar, Type

from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from models.base import Base as BaseModel


ModelType = TypeVar('ModelType', bound=BaseModel)


class CRUDBase(Generic[ModelType]):
    _model: Type[ModelType]

    @classmethod
    async def create(cls, session: AsyncSession, instance) -> ModelType:
        instance_obj = cls._model(**instance.model_dump())
        session.add(instance_obj)
        try:
            await session.commit()
        except IntegrityError as e:
            await session.rollback()
            print(e)
        await session.refresh(instance_obj)
        return instance_obj