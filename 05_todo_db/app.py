'''
代办清单 v4 Web 版：
功能：浏览器访问，支持添加，标记完成，删除任务
数据存储：SQLite 数据库
'''

from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'todo.db')

# 初始化数据库，如果不存在就创建
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        done INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

# 读取所有任务
def load_tasks():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, done FROM tasks ORDER BY id DESC')
    tasks = cursor.fetchall()
    conn.close()
    # 转化为列表字典，方便模板用
    return [{'id': t[0], 'name': t[1], 'done': t[2]} for t in tasks]

# 首页
@app.route('/')
def index():
    tasks = load_tasks()
    return render_template('index.html', tasks=tasks)

# 添加任务
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task_name')
    if task_name:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO tasks (name, done) VALUES (?, ?)', (task_name, 0))
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

# 标记完成任务
@app.route('/done', methods=['POST'])
def done_task():
    task_id = request.form.get('task_id')
    if task_id:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f'UPDATE tasks SET done = 1 WHERE id = {task_id}')
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

# 删除任务
@app.route('/delete', methods=['POST'])
def delete_task():
    task_id = request.form.get('task_id')
    if task_id:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute(f'DELETE FROM tasks WHERE id = {task_id}')
        conn.commit()
        conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)