'''
代办清单 v3 Web 版：
功能：浏览器访问，支持添加，标记完成，删除任务
数据存储：JSON文件
'''


import os
import json

from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

# 读取任务数据
def load_tasks():
    if os.path.exists('task_sheet.json'):
        with open('task_sheet.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

# 保存任务数据
def dump_tasks(tasks):
    with open('task_sheet.json', 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


# 首页：显示所有任务
@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

# 添加任务
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    if task_name:
        tasks = load_tasks()
        tasks[task_name] = 0
        dump_tasks(tasks)
    return redirect(url_for('index'))

# 标记任务为已完成
@app.route('/done', methods=['POST'])
def done_task():
    task_name = request.form.get('task_name')
    tasks = load_tasks()
    tasks[task_name] = 1
    dump_tasks(tasks)
    return redirect(url_for('index'))

# 删除任务
@app.route('/delete', methods=['POST'])
def delete_task():
    task_name = request.form.get('task_name')
    tasks = load_tasks()
    del tasks[task_name]
    dump_tasks(tasks)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)