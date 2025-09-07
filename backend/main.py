from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models import user, course, like, comment
from routers import auth, courses, likes, comments

app = FastAPI(title="E-Learning Platform Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)
like.Base.metadata.create_all(bind=engine)
comment.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(likes.router, prefix="/likes", tags=["likes"])
app.include_router(comments.router, prefix="/comments", tags=["comments"])

@app.get("/")
async def root():
    return {"message": "E-Learning Platform Backend"}