Fitness Center API
A Flask-based API for managing members and workout sessions in a fitness center, using Flask-SQLAlchemy for ORM.

Features
Add, update, view, and delete members.

Schedule, update, and view workout sessions.

RESTful endpoints with proper JSON responses.

Setup
Clone the repository:

bash
git clone https://github.com/your-username/fitness-center-api.git
cd fitness-center-api
Set up a virtual environment:

bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Configure the database URI in app.py, initialize the database, and run:

bash
python app.py
Endpoints
Members: POST /members, GET /members, PUT /members/<id>, DELETE /members/<id>

Workout Sessions: POST /workouts, GET /members/<member_id>/workouts, PUT /workouts/<id>
