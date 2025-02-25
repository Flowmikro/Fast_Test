from fastapi import FastAPI

from tasks.router import router

app = FastAPI(name='TaskAPI')

app.include_router(prefix='/api/tasks', router=router, tags=['Task'])
