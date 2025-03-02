""" Initializes a task object """

class Task:
    def __init__(self, id, title, description, status, due_date, priority, category):
        #Инициализация задачи
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.due_date = due_date
        self.priority = priority
        self.category = category

    def __repr__(self):
        return f"<Task {self.id}: {self.title}>"