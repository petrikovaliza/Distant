import pytest
from my_src.task_manager import TaskManager
from my_src.models import Task

# Подменяем реальный доступ к базе данных фиктивным
class MockDatabase:
    def load_from_db(self):
        return []
    
    def save_to_db(self, tasks):
        pass

@pytest.fixture
def task_manager():
    # Фикстура для создания экземпляра TaskManager"""
    mock_db = MockDatabase()
    return TaskManager(mock_db)

def test_create_task(task_manager):
    # Тестирование метода create_task"""
    # Создаем новую задачу
    new_task = task_manager.create_task("Новая задача", "Описание задачи", "01-01-2025", "Высокий", "Работа")
    
    assert len(task_manager.get_all_tasks()) == 1
    assert isinstance(new_task, Task)
    assert new_task.title == "Новая задача"
    assert new_task.description == "Описание задачи"
    assert new_task.due_date == "01-01-2025"
    assert new_task.priority == "Высокий"
    assert new_task.category == "Работа"

def test_get_all_tasks(task_manager):
    #Тестирование метода get_all_tasks"""
    # Проверка начального состояния (без задач)
    assert len(task_manager.get_all_tasks()) == 0
    
    # Добавляем несколько задач
    task_1 = task_manager.create_task("Первая задача", "", "01-02-2025", "Средний", "Домашние дела")
    task_2 = task_manager.create_task("Вторая задача", "", "03-04-2026", "Низкий", "Учеба")
    
    all_tasks = task_manager.get_all_tasks()
    assert len(all_tasks) == 2
    assert all_tasks[0].title == "Первая задача"
    assert all_tasks[1].title == "Вторая задача"

def test_update_status(task_manager):
    # Тестирование метода update_status"""
    # Создаем задачу
    task = task_manager.create_task("Задача для обновления", "", "05-06-2027", "Средний", "Работа")
    
    # Обновление статуса
    updated_task = task_manager.update_status(1, "Выполнено")
    
    assert updated_task.status == "Выполнено"
    assert task_manager.get_all_tasks()[0].status == "Выполнено"

    # Проверка исключения при неверном ID
    with pytest.raises(ValueError):
        task_manager.update_status(9999, "Не выполнено")

def test_delete_task(task_manager):
    # Тестирование метода delete_task"""
    # Создаем две задачи
    task_1 = task_manager.create_task("Удаляемая задача", "", "07-08-2028", "Высокий", "Личное")
    task_2 = task_manager.create_task("Оставшаяся задача", "", "09-10-2029", "Низкий", "Покупки")
    
    # Удаляем первую задачу
    task_manager.delete_task(1)
    
    remaining_tasks = task_manager.get_all_tasks()
    assert len(remaining_tasks) == 1
    assert remaining_tasks[0].id == 2
    assert remaining_tasks[0].title == "Оставшаяся задача"

    # Проверка исключения при неверном ID
    with pytest.raises(ValueError):
        task_manager.delete_task(99)

def test_search_tasks(task_manager):
    #Тестирование метода search_tasks"""
    # Создаем три задачи
    task_1 = task_manager.create_task("Поисковая задача", "описание поиска", "11-12-2030", "Средний", "Спорт")
    task_2 = task_manager.create_task("Другая задача", "другое описание", "13-14-2031", "Низкий", "Чтение")
    task_3 = task_manager.create_task("Третья задача", "поисковое описание", "15-16-2032", "Высокий", "Кулинария")
    
    # Поиск по ключевому слову 'поиск'
    search_results = task_manager.search_tasks('поиск')
    assert len(search_results) == 2
    assert search_results[0].title == "Поисковая задача"
    assert search_results[1].title == "Третья задача"

    # Поиск по несуществующему ключевому слову
    empty_results = task_manager.search_tasks('несуществующее слово')
    assert len(empty_results) == 0

def test_save_to_db(task_manager):
    """Тестирование метода save_to_db"""
    # Метод save_to_db не имеет возвращаемого значения, проверим, что он вызывается корректно
    task_manager.save_to_db()