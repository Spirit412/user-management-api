from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict

class BaseSchema(BaseModel):
    """Base Schema with ORM mode enabled."""
    model_config = ConfigDict(from_attributes=True)

class UserSchema(BaseSchema):
    id: int
    name: str
    surname: str
    created_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseSchema):
    name: str
    surname: str
    password: str


class UserUpdateSchema(BaseSchema):
    name: Optional[str] = None
    surname: Optional[str] = None
    password: Optional[str] = None
