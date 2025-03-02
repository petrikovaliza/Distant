import sqlite3
from models import Task

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('tasks.db')
        self.cursor = self.conn.cursor()
        self._create_table()

    def _create_table(self):
        # Создание таблицы задач, если она еще не существует
        query = """ CREATE TABLE IF NOT EXISTS tasks ( id INTEGER PRIMARY KEY, title TEXT, description TEXT, status TEXT, due_date TEXT, priority TEXT, category TEXT ) """
        self.cursor.execute(query)
        self.conn.commit()

    def load_from_db(self):
        # Загрузка задач из базы данных
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        tasks = [Task(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]
        return tasks
    
    def save_to_db(self, tasks):
        # Сохранение задач в базу данных
        self.cursor.executemany(
            "INSERT OR REPLACE INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?)",
            [(task.id, task.title, task.description, task.status, task.due_date, task.priority, task.category) for task in tasks]
        )
        self.conn.commit()