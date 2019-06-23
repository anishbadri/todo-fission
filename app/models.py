from app import db
from datetime import datetime



class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100), index=True)
    # time = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    todos = db.relationship('Todo', backref='task', lazy='dynamic')
    def __repr__(self):
        return 'Task -' + self.task


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_task = db.Column(db.String(100), index=True)
    time = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=False)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return 'Todo -' + self.todo_task



    



