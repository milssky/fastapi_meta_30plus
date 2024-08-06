from pydantic import BaseModel


class TaskWrite(BaseModel):
    name: str
    description: str