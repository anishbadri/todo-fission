from flask import render_template, redirect, url_for
from app import app, db
from app.forms import AddTask, AddTodo
from app.models import Task, Todo

# list=[]
# completed = []

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddTask()
    form2 = AddTodo()
    # newtaskTime = None
    if form.validate_on_submit():
        newTask = form.newtask.data
        # if form.time.data:
        #     newtaskTime = form.time.data   
        newTask = Task(task=newTask)       
        db.session.add(newTask)  
        db.session.commit()
        return redirect(url_for('index'))

    if form2.validate_on_submit():
        print(form2.taskid.data, form2.newtodo.data)
    taskList = Task.query.all()
    completed = Task.query.filter_by(status=1)
    return render_template('index.html', title='Home', form=form, task=taskList, completed = completed, form2=form2)


@app.route('/markcomplete/<int:id>')
def markComplete(id):
    complete = Task.query.get(id)
    complete.status = 1
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/markincomplete/<int:id>')
def markInComplete(id):
    incomplete = Task.query.get(id)
    incomplete.status = 0
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update-task-status/<int:id>', methods=['POST'])
def updateTaskStatus(id):
    task = Task.query.get(id)
    task.status = 0 if task.status == 1 else 1
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update-todo-status/<int:id>', methods=['POST'])
def updateTodoStatus(id):
    todo = Todo.query.get(id)
    todo.status = 0 if todo.status == 1 else 1
    db.session.commit()
    return redirect(url_for('index'))
    
@app.route('/todofission/<int:id>', methods=['POST','GET'])
def todoFission(id):
    form = AddTodo()
    task = Task.query.get(id)
    if form.validate_on_submit() and task:
        newTodoItem = form.newtodo.data
        newtodoTime = form.time.data
        newTodo = Todo(todo_task=newTodoItem, time= newtodoTime, task_id = task.id)
        db.session.add(newTodo)
        db.session.commit() 
        return redirect(url_for('index'))         
    return 'Failed'

# def addTodo():
#     newtoData = 
#     task = Task.query.get(id)
#     newTodo = Todo(todo_task = newtoData, ) //notimefornow

# @app.route('/deleteTodo/<int:id>')
# def deleteTodo(id):
#         Todo.query.get(id)

@app.route("/home")
def home():
    return render_template('home.html')

