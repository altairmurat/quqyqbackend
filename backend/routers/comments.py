from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.comment import Comment as CommentModel
from schemas.comment import Comment, CommentCreate
from routers.auth import get_current_user
from models.user import User

router = APIRouter()

@router.get("/lesson/{lesson_id}", response_model=List[Comment])
async def get_comments(lesson_id: int, db: Session = Depends(get_db)):
    return db.query(CommentModel).filter(CommentModel.lesson_id == lesson_id).all()

@router.post("/", response_model=Comment)
async def create_comment(comment: CommentCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_comment = CommentModel(
        user_id=current_user.id,
        lesson_id=comment.lesson_id,
        text=comment.text
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment