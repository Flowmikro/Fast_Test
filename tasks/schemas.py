from pydantic import BaseModel


class TaskSchema(BaseModel):
    title: str
    description: str | None


class TaskSchemaPUT(BaseModel):
    title: str | None
    description: str | None
