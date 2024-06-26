from datetime import datetime
from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import Optional


class TodoBase(BaseModel):
    description: str = Field(..., min_length=1)
    completed: Optional[bool] = Field(default=False)


class TodoCreate(TodoBase):
    pass


class TodoUpdate(TodoBase):
    pass


class TodoInDB(TodoBase):
    id: int
    date_created: datetime

    class Config:
        from_attribute = True
