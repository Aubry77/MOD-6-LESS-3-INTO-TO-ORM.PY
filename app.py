from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Fitness Center API is running!"@app.route('/members', methods=['POST'])
def add_member():
    data = request.get_json()  # Get data from the client
    new_member = Member(name=data['name'], age=data['age'], email=data['email'])
    db.session.add(new_member)
    db.session.commit()
    return jsonify({"message": "Member added successfully!"}), 201

@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    members_list = [{"id": m.id, "name": m.name, "age": m.age, "email": m.email} for m in members]
    return jsonify(members_list), 200

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    member = Member.query.get_or_404(id)
    member.name = data.get('name', member.name)
    member.age = data.get('age', member.age)
    member.email = data.get('email', member.email)
    db.session.commit()
    return jsonify({"message": "Member updated successfully!"}), 200

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = Member.query.get_or_404(id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member deleted successfully!"}), 200


@app.route('/workouts', methods=['POST'])
def schedule_workout():
    data = request.get_json()
    new_session = WorkoutSession(
        member_id=data['member_id'],
        session_date=data['session_date'],
        duration=data['duration'],
        description=data['description']
    )
    db.session.add(new_session)
    db.session.commit()
    return jsonify({"message": "Workout session scheduled!"}), 201

@app.route('/members/<int:member_id>/workouts', methods=['GET'])
def get_workouts_for_member(member_id):
    sessions = WorkoutSession.query.filter_by(member_id=member_id).all()
    sessions_list = [
        {
            "id": s.id,
            "session_date": s.session_date,
            "duration": s.duration,
            "description": s.description
        }
        for s in sessions
    ]
    return jsonify(sessions_list), 200

@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.get_json()
    session = WorkoutSession.query.get_or_404(id)
    session.session_date = data.get('session_date', session.session_date)
    session.duration = data.get('duration', session.duration)
    session.description = data.get('description', session.description)
    db.session.commit()
    return jsonify({"message": "Workout session updated!"}), 200

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

if __name__ == '__main__':
    app.run(debug=True)
