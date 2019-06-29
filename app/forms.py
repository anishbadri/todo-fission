from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddTask(FlaskForm):
    newtask = StringField('Add a Task', validators=[DataRequired()])
    # time = StringField('Time')
    add = SubmitField('Add')


class AddTodo(FlaskForm):
    taskid = None
    newtodo = StringField('Add a Todo', validators=[DataRequired()])
    time = StringField('Time Required')
    add = SubmitField('Add')