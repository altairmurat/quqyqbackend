from pydantic import BaseModel

class LikeBase(BaseModel):
    lesson_id: int
    is_liked: bool

class LikeCreate(LikeBase):
    pass

class Like(LikeBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True