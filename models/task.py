from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from core.db import Base


class Task(Base):
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)