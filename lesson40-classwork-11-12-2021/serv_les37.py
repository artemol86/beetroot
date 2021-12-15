from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/task', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        title = request.form['title']
        priority = int(request.form['priority'])
        new_task = Task(title=title, priority=priority)
    else:
        order = request.args.get(
            'order', default = '', type = str)
        if order:
            tasks = [] #копія Task.objects
            bubble_sort(tasks, order) #Y.T.L24 (27.11.2021) 49:09 - сортируем уже существующие ТАСКИ
        else:
            insertion_sort(tasks)
    return render_template('task_list.html', tasks=tasks) #Y.T.L24 (27.11.2021) 48:21
'''
def create_app():
    template_dir = os.path.abspath('templates')
    app = Flask(__name__, template_folder=template_dir)

    from . import task
    app.register_blueprint(task.bp)

    return app