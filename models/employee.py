import json


class Employee:
    def __init__(self, employee_id, name, position):
        self.employee_id = employee_id
        self.name = name
        self.position = position

    def get_details(self):
        employee_info = {
            "employee_id": self.employee_id,
            "name": self.name,
            "position": self.position
        }
        return employee_info

    def __str__(self):
        return str(self.get_details())

    def __repr__(self):
        return f'Employee({self.employee_id}, {self.name!r}, {self.position})'

class Manager(Employee):
    def __init__(self, employee_id, name, department):
        super().__init__(employee_id=employee_id, name=name, position="Manager")
        self.department = department

    def change_department(self, new_department):
        self.department = new_department if new_department else "Undefined"

    def get_details(self):
        partner_info = super().get_details()
        partner_info["department"] = self.department
        return partner_info

    def __repr__(self):
        return f'Manager({self.employee_id}, {self.name!r}, {self.department})'