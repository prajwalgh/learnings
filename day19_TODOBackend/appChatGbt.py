from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Recommended setting to avoid overhead
db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Priority(db.Model):
    priority_id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.String(50), nullable=False)
    color = db.Column(db.String(7), nullable=False)

class Task(db.Model):
    task_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    priority_id = db.Column(db.Integer, db.ForeignKey('priority.priority_id'))
    deadline = db.Column(db.DateTime)
    repetitive = db.Column(db.Boolean, default=False)
    repeat_interval = db.Column(db.String(50))

class Reminder(db.Model):
    reminder_id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'), nullable=False)
    reminder_time = db.Column(db.DateTime, nullable=False)
    message = db.Column(db.String(255))

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task(
        user_id=data['user_id'],
        title=data['title'],
        description=data.get('description'),
        category_id=data.get('category_id'),
        priority_id=data.get('priority_id'),
        deadline=datetime.strptime(data['deadline'], '%Y-%m-%dT%H:%M:%S'),
        repetitive=data.get('repetitive', False),
        repeat_interval=data.get('repeat_interval')
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created successfully"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

