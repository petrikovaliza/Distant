import sys
from task_manager import TaskManager

""" Script for task management via console menu. 
This script implements a simple console application for task management.
The user can add new tasks, view a list of all tasks, 
change their statuses, delete tasks and search for tasks by keywords. 
The script requires a connection to an SQLite database. """

def main():
    manager = TaskManager()
    
    while True:
        print("Меню:")
        print("1. Добавить задачу")
        print("2. Показать все задачи")
        print("3. Изменить статус задачи")
        print("4. Удалить задачу")
        print("5. Поиск задач")
        print("6. Выход")
        
        try:
            choice = int(input("Ваш выбор: "))
            
            if choice == 1:
                title = input("Название задачи: ")
                description = input("Описание задачи: ")
                due_date = input("Срок выполнения (YYYY-MM-DD): ")
                priority = input("Приоритет (низкий/средний/высокий): ")
                category = input("Категория (работа/учеба/личное): ")
                
                manager.create_task(title, description, due_date, priority, category)
                print("Задача добавлена успешно!")
                
            elif choice == 2:
                tasks = manager.get_all_tasks()
                for task in tasks:
                    print(f"{task.id}. {task.title}: {task.description}")
                    print(f"Статус: {task.status}, Срок: {task.due_date}, Приоритет: {task.priority}, Категория: {task.category}\n")
                    
            elif choice == 3:
                task_id = int(input("ID задачи: "))
                status = input("Новый статус (не выполнено/в процессе/выполнено): ")
                manager.update_status(task_id, status)
                print("Статус обновлен успешно!")
                
            elif choice == 4:
                task_id = int(input("ID задачи: "))
                manager.delete_task(task_id)
                print("Задача удалена успешно!")
                
            elif choice == 5:
                keyword = input("Ключевое слово для поиска: ")
                results = manager.search_tasks(keyword)
                for result in results:
                    print(f"{result.id}. {result.title}: {result.description}")
                    print(f"Статус: {result.status}, Срок: {result.due_date}, Приоритет: {result.priority}, Категория: {result.category}\n")
                
            elif choice == 6:
                manager.save_to_db()
                print("До свидания!")
                break
                
            else:
                print("Неверный выбор. Попробуйте снова.")
                
        except ValueError:
            print("Пожалуйста, введите число.")


if __name__ == "__main__":
    main()