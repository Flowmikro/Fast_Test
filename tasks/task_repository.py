from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import HTTPException, status

from tasks.models import TaskModel
from tasks.schemas import TaskSchema, TaskSchemaPUT


class TaskRepository:
    @staticmethod
    async def get_all_tasks(session: AsyncSession):
        result = await session.execute(select(TaskModel).order_by(TaskModel.created_at))
        return result.scalars().all()

    @staticmethod
    async def get_task_by_id(session: AsyncSession, task_id: int):
        result = await session.get(TaskModel, task_id)
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return result

    @staticmethod
    async def add_task(session: AsyncSession, task: TaskSchema):
        try:
            db_task = TaskModel(**task.model_dump())
            session.add(db_task)
            await session.commit()
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Task with this title already exists")

    @staticmethod
    async def update_task(session: AsyncSession, task_id: int, task: TaskSchemaPUT):
        db_task = await session.get(TaskModel, task_id)
        if not db_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        for attr, value in task.model_dump().items():
            setattr(db_task, attr, value)
        await session.commit()
        await session.refresh(db_task)
        return db_task

    @staticmethod
    async def delete_task(session: AsyncSession, task_id: int):
        db_task = await session.get(TaskModel, task_id)
        if not db_task:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        await session.delete(db_task)
        await session.commit()
