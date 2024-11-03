from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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

    def as_dict(self):
        return {
            'task_id': self.task_id,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'category_id': self.category_id,
            'priority_id': self.priority_id,
            'deadline': self.deadline.isoformat() if self.deadline else None,
            'repetitive': self.repetitive,
            'repeat_interval': self.repeat_interval
        }


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
        deadline=datetime.strptime(data['deadline'], '%Y-%m-%dT%H:%M:%S') if 'deadline' in data else None,
        repetitive=data.get('repetitive', False),
        repeat_interval=data.get('repeat_interval')
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created successfully"}), 201


@app.route('/tasks/<int:user_id>', methods=['GET'])
def get_tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.as_dict() for task in tasks])


@app.route('/tasks/<int:user_id>/recommend', methods=['GET'])
def get_recommended_tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    high_priority_tasks = [task for task in tasks if task.priority_id == 1]

    if high_priority_tasks:
        # Sorting high priority tasks by deadline if they exist
        high_priority_tasks.sort(key=lambda task: task.deadline)
        return jsonify(high_priority_tasks[0].as_dict())

    # If no high priority tasks, return all tasks
    return jsonify([task.as_dict() for task in tasks])


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({"message": "Task not found"}), 404

    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.category_id = data.get('category_id', task.category_id)
    task.priority_id = data.get('priority_id', task.priority_id)
    if 'deadline' in data:
        task.deadline = datetime.strptime(data['deadline'], '%Y-%m-%dT%H:%M:%S')
    task.repetitive = data.get('repetitive', task.repetitive)
    task.repeat_interval = data.get('repeat_interval', task.repeat_interval)

    db.session.commit()
    return jsonify({"message": "Task updated successfully"}), 200


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({"message": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
