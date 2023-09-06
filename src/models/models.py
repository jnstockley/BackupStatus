from sqlalchemy import String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Folder(Base):
    __tablename__ = 'folder'

    id: Mapped[int] = mapped_column(primary_key=True)
    path: Mapped[str] = mapped_column(String)
    friendly_name: Mapped[str] = mapped_column(String(50))
    last_update: Mapped[DateTime] = mapped_column(DateTime)
