from sqlalchemy.orm import Session
from database import SessionLocal, Base, engine
from models.course import Course, Lesson

def init_db():
    
    Base.metadata.create_all(bind=SessionLocal().bind)
    
    db = SessionLocal()
    try:
        course1 = Course(title="Quqyq")
        db.add(course1)
        db.commit()
        db.refresh(course1)
        lesson1 = Lesson(course_id=course1.id, title="Quqyk Basics", video_url="https://www.w3schools.com/html/mov_bbb.mp4", transcript="This course is about quqyk...")
        lesson2 = Lesson(course_id=course1.id, title="Quqyq ququq", video_url="https://www.w3schools.com/html/mov_bbb.mp4", transcript="Do your best not to be caught by police...")
        db.add_all([lesson1, lesson2])
        
        course2 = Course(title="Quqyq olympiad prep")
        db.add(course2)
        db.commit()
        db.refresh(course2)
        lesson3 = Lesson(course_id=course2.id, title="Questions", video_url="https://www.w3schools.com/html/mov_bbb.mp4", transcript="Learn the fundamentals of Quqyq...")
        db.add(lesson3)
        
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()