from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AddToDo(FlaskForm):
    newtodo = StringField('Add a To-Do', validators=[DataRequired()])
    