E-Learning Platform Backend

This is a FastAPI backend for an e-learning platform, handling user authentication, courses, lessons, likes, and comments. It uses SQLite as the database and SQLAlchemy as the ORM. The frontend is located in the frontend/ directory.

Setup Instructions





Clone the repository (if applicable):

git clone <repository-url>
cd elearning-platform



Create a virtual environment:





On Windows (PowerShell):

python -m venv venv
.\venv\Scripts\activate



On Windows (Command Prompt):

python -m venv venv
venv\Scripts\activate



On Linux/MacOS:

python -m venv venv
source venv/bin/activate



Install dependencies:

pip install -r backend/requirements.txt



Populate initial data:





Run the initialization script to populate the database:

python backend/init_db.py



Run the backend:

cd backend
uvicorn main:app --reload



Run the frontend:





Open frontend/index.html in a browser (e.g., via VS Code's "Open with Live Server" extension).



Alternatively, serve it using a simple HTTP server:

cd frontend
python -m http.server 8080



Access the frontend at http://localhost:8080.

API Endpoints





Auth:





POST /auth/register: Register a new user (email, password).



POST /auth/token: Login and get JWT token.



Courses:





GET /courses/: List all courses.



GET /courses/{course_id}: Get a specific course with lessons.



POST /courses/: Create a new course with lessons.



Likes:





GET /likes/lesson/{lesson_id}: Get all likes for a lesson.



POST /likes/: Toggle like for a lesson (requires authentication).



Comments:





GET /comments/lesson/{lesson_id}: Get all comments for a lesson.



POST /comments/: Post a new comment (requires authentication).

Notes





Replace SECRET_KEY in backend/routers/auth.py with a secure key for production.



Update CORS allow_origins in backend/main.py to ["http://localhost:8080"] for production.



The SQLite database file (elearning.db) will be created in the project root.