from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app_config.session_manager import get_session
from .schemas import TaskSchema, TaskSchemaPUT
from .task_repository import TaskRepository

router = APIRouter()


@router.get('/v1')
async def get_tasks(session: AsyncSession = Depends(get_session)) -> JSONResponse:
    """
    Получение списка задач
    """
    tasks = await TaskRepository.get_all_tasks(session)
    return JSONResponse(content={"data": jsonable_encoder(tasks)}, status_code=status.HTTP_200_OK)


@router.get('/v1/{task_id}')
async def get_task(task_id: int, session: AsyncSession = Depends(get_session)):
    """
    Получение информации о задаче по ID
    """
    task = await TaskRepository.get_task_by_id(session, task_id)
    return JSONResponse(content={"data": jsonable_encoder(task)}, status_code=status.HTTP_200_OK)


@router.post('/v1')
async def add_task(task: TaskSchema, session: AsyncSession = Depends(get_session)):
    """
    Добавление новой задачи
    """
    await TaskRepository.add_task(session, task)
    return JSONResponse(content={"data": jsonable_encoder(task)}, status_code=status.HTTP_201_CREATED)


@router.put('/v1/{task_id}')
async def edit_task(task_id: int, task: TaskSchemaPUT, session: AsyncSession = Depends(get_session)):
    """
    Обновление задачи
    """
    updated_task = await TaskRepository.update_task(session, task_id, task)
    return JSONResponse(content={"data": jsonable_encoder(updated_task)}, status_code=status.HTTP_200_OK)


@router.delete('/v1/{task_id}')
async def delete_task(task_id: int, session: AsyncSession = Depends(get_session)):
    """
    Удаление задачи
    """
    await TaskRepository.delete_task(session, task_id)
    return JSONResponse(content=None, status_code=status.HTTP_204_NO_CONTENT)
