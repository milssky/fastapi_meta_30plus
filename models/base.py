from sqlalchemy.orm import (
    DeclarativeBase, 
    Mapped, 
    declared_attr,
    mapped_column 
)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
