from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.course import Course as CourseModel, Lesson as LessonModel
from schemas.course import Course, CourseCreate, Lesson
import re

router = APIRouter()

@router.get("/", response_model=List[Course])
async def get_courses(db: Session = Depends(get_db)):
    return db.query(CourseModel).all()

@router.get("/{course_id}", response_model=Course)
async def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.post("/", response_model=Course)
async def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = CourseModel(title=course.title)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    for lesson in course.lessons:
        video_url = lesson.video_url
        if "youtube.com/watch" in video_url or "youtu.be" in video_url:
            match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})(?:\?|&|$)")  # More robust pattern
            video_id = match.group(1) if match else None
            if video_id:
                video_url = f"https://www.youtube.com/embed/{video_id}?rel=0"  # ?rel=0 hides related videos
            else:
                raise HTTPException(status_code=400, detail="Invalid YouTube URL")
        db_lesson = LessonModel(
            course_id=db_course.id,
            title=lesson.title,
            video_url=video_url,
            transcript=lesson.transcript
        )
        db.add(db_lesson)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.delete("/{course_id}")
async def delete_course(course_id: int, db: Session = Depends(get_db)):
    try:
        course = db.query(CourseModel).filter(CourseModel.id == course_id).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        db.delete(course)
        db.commit()
        return {"message": f"Course {course_id} and its lessons have been deleted"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to delete course: {str(e)}")