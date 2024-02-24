import json


class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position

    def save_to_json(self, file_name):
        employee_info = {
            "employee_id": self.employee_id,
            "name": self.name,
            "position": self.position
        }
        # Ошибка: отсутствует обработка исключений при работе с файлом
        with open(file_name, 'w') as file:
            json.dump(employee_info, file, ensure_ascii=False, indent=4)


class Manager(Employee):
    def __init__(self, employee_id, name, department):
        super().__init__(employee_id=employee_id, name=name, position="Manager")
        self.department = department

    def save_to_json(self, file_name):
        manager_info = super().save_to_json(file_name)  # Ошибка: метод родителя не возвращает данные
        manager_info.update({"department": self.department})  # Эта строка не будет работать как ожидается
        # Повторение ошибки обработки ошибок при работе с файлом
        with open(file_name, 'w') as file:
            json.dump(manager_info, file, ensure_ascii=False, indent=4)

    def change_department(self, new_department):
        # Ошибка безопасности данных: прямое присваивание нового отдела без проверки
        self.department = new_department if new_department else "Undefined"
