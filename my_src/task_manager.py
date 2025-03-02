from models import Task
from database.db import Database

""" Task Management Module. This module contains the TaskManager class,
 which allows you to manage the list of tasks, including creating new tasks, getting all tasks, 
 changing the status of a task, deleting a task, and searching for tasks by keyword. """

class TaskManager:
    def __init__(self):
        self.db = Database()
        self.tasks = self.db.load_from_db()

    def create_task(self, title, description, due_date, priority, category):
        # Создание новой задачи
        new_task = Task(len(self.tasks) + 1, title, description, "не выполнено", due_date, priority, category)
        self.tasks.append(new_task)
        return new_task

    def get_all_tasks(self):
        # Получение всех задач
        return self.tasks

    def update_status(self, task_id, status):
        # Изменение статуса задачи
        for task in self.tasks:
            if task.id == task_id:
                task.status = status
                return task
        raise ValueError(f"Задача с ID {task_id} не найдена")

    def delete_task(self, task_id):
        # Удаление задачи
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                return
        raise ValueError(f"Задача с ID {task_id} не найдена")

    def search_tasks(self, keyword):
        # Поиск задач по ключевому слову
        results = []
        for task in self.tasks:
            if keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower():
                results.append(task)
        return results

    def save_to_db(self):
        # Сохранение задач в базу данных
        self.db.save_to_db(self.tasks)
