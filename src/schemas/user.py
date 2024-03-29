import uuid
from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from src.models.models import Role


class UserSchema(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(min_length=6, max_length=8)


class UserResponse(BaseModel):
    id: uuid.UUID
    username: str
    email: EmailStr
    role: Role

    class Config:
        from_attributes = True


class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    
class RequestEmail(BaseModel):
    email: EmailStr
    
class UserResetPassword(BaseModel):
    password1: str = Field(min_length=6, max_length=8)
    password2: str = Field(min_length=6, max_length=8)