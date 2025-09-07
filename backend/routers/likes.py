from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models.like import Like as LikeModel
from schemas.like import Like, LikeCreate
from routers.auth import get_current_user
from models.user import User

router = APIRouter()

@router.get("/lesson/{lesson_id}", response_model=List[Like])
async def get_likes(lesson_id: int, db: Session = Depends(get_db)):
    return db.query(LikeModel).filter(LikeModel.lesson_id == lesson_id).all()

@router.post("/", response_model=Like)
async def toggle_like(like: LikeCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    existing_like = db.query(LikeModel).filter(
        LikeModel.user_id == current_user.id,
        LikeModel.lesson_id == like.lesson_id
    ).first()
    if existing_like:
        existing_like.is_liked = like.is_liked
        db.commit()
        db.refresh(existing_like)
        return existing_like
    db_like = LikeModel(
        user_id=current_user.id,
        lesson_id=like.lesson_id,
        is_liked=like.is_liked
    )
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like