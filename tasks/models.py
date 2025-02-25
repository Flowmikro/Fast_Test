import pytz
from datetime import datetime

from sqlalchemy import String, Integer, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column

from app_config.session_manager import Base

MSK_TZ = pytz.timezone("Europe/Moscow")


def msk_now():
    return datetime.now(MSK_TZ)


class TaskModel(Base):
    __tablename__ = "task"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=msk_now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=msk_now, onupdate=msk_now)

    def __repr__(self):
        return f"<TaskModel(id={self.id})>"
