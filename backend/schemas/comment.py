from pydantic import BaseModel
from datetime import datetime

class CommentBase(BaseModel):
    text: str
    lesson_id: int

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True