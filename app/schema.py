
from datetime import date, datetime
from distutils.util import strtobool
from typing import Optional
from pydantic import BaseModel, EmailStr, conint

from app.database import Base


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class Post(BaseModel):
    title: str
    content: str
    published: bool
    created_at: datetime
    owner_id: int
    owner: User

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    phone_number: str


class CreatedUser(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type = str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    id: int
    dir: conint(ge=0, le=1)


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True
