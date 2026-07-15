import os
import json

from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

def load_tasks():
    if os.path.exists('task_sheet.json'):
        with open('task_sheet.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def dump_tasks(tasks):
    with open('task_sheet.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)



@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    if task_name:
        tasks = load_tasks()
        tasks[task_name] = 0
        dump_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/done', methods=['POST'])
def done_task():
    task_name = request.form.get('task_name')
    tasks = load_tasks()
    tasks[task_name] = 1
    dump_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_task():
    task_name = request.form.get('task_name')
    tasks = load_tasks()
    del tasks[task_name]
    dump_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)