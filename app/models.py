from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from datetime import datetime
from typing import List

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'


    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)

    tasks: Mapped[List[Task]] = relationship(back_populates='user')



class Task(Base):
    __tablename__ = 'task'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    created_at: Mapped[datetime] = mapped_column(default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(nullable=True, default=None)
    deadline: Mapped[datetime] = mapped_column(nullable=True, default = None)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'))


    user: Mapped[User] = relationship(back_populates='tasks')