from enum import StrEnum

from pydantic import BaseModel, Field


__all__ = ['User', 'UserRole', 'UserToCreate']


class UserRole(StrEnum):
    ADMIN = 'admin'
    TEACHER = 'teacher'
    PUPIL = 'pupil'
    STUDENT = 'student'


class BaseUser(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=0, le=400)
    role: UserRole


class UserToCreate(BaseUser):
    pass


class User(BaseUser):
    id: int
