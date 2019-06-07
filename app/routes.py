from flask import render_template
from app import app
from app.forms import AddToDo

list=[]

@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddToDo()
    if form.validate_on_submit():
        list.append(form.newtodo.data)
        form.newtodo.data = ''
    return render_template('index.html', title='Home', form=form, list=list)
    




