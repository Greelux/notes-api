from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class NoteCreate(BaseModel):
    title: str
    content_markdown: str
    tags: str = ""


class NoteResponse(BaseModel):
    id: int
    title: str
    content_markdown: str
    tags: str
    created_at: datetime

    class Config:
        from_attributes = True