from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] 
    first_name: str
    last_name: str
    middle_name: Optional[str]
    gender: Gender
    roles = list[Role]
