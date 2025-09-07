from pydantic import BaseModel
from typing import List

class LessonBase(BaseModel):
    title: str
    video_url: str
    transcript: str

class LessonCreate(LessonBase):
    pass

class Lesson(LessonBase):
    id: int
    course_id: int

    class Config:
        from_attributes = True

class CourseBase(BaseModel):
    title: str

class CourseCreate(CourseBase):
    lessons: List[LessonCreate]

class Course(CourseBase):
    id: int
    lessons: List[Lesson]

    class Config:
        from_attributes = True