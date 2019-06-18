from flask import render_template, redirect, url_for
from app import app, db
from app.forms import AddToDo
from app.models import Todo

# list=[]
# completed = []

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddToDo()
    newtaskTime = None
    if form.validate_on_submit():
        newTask = form.newtodo.data
        if form.time.data:
            newtaskTime = form.time.data   
        newTodo = Todo(task=newTask, time=newtaskTime)       
        db.session.add(newTodo)  
        db.session.commit()
        return redirect(url_for('index'))
    list = Todo.query.filter_by(status=0)
    completed = Todo.query.filter_by(status=1)
    return render_template('index.html', title='Home', form=form, list=list, completed = completed)


@app.route('/markcomplete/<int:id>')
def markComplete(id):
    complete = Todo.query.get(id)
    complete.status = 1
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/markincomplete/<int:id>')
def markInComplete(id):
    incomplete = Todo.query.get(id)
    incomplete.status = 0
    db.session.commit()
    return redirect(url_for('index'))
    

@app.route('/deleteTodo/<int:id>')
def deleteTodo(id):
        Todo.query.get(id)



