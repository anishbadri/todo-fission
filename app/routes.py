from flask import render_template, redirect, url_for
from app import app, db
from app.forms import AddToDo
from app.models import Todo

class todo:
    def __init__(self, task, time = None):
        self.task = task
        self.time = time

# list=[]
completed = []

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddToDo()
    newtaskTime = None
    if form.validate_on_submit():
        newTask = todo(form.newtodo.data)
        if form.time.data:
            newtaskTime = form.time.data   
        newTodo = Todo(task=newTask, time=newtaskTime)       
        db.session.add(newTodo)  
        db.session.commmit()
        return redirect(url_for('index'))
    list = Todo.query.all()
    return render_template('index.html', title='Home', form=form, list=list, completed = completed)


@app.route('/markcomplete/<int:id>')
def markComplete(id):
    completed.append(list.pop(id))
    return redirect(url_for('index'))

@app.route('/markincomplete/<int:id>')
def markInComplete(id):
    list.append(completed.pop(id))
    return redirect(url_for('index'))
    




