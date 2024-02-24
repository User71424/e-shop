import json


class Partner:
    def __init__(self, partner_id, email, name, phone_number):
        self.partner_id = partner_id
        self.email = email
        self.name = name
        self.phone_number = phone_number

    def save_to_json(self, file_name):
        partner_info = {
            "partner_id": self.partner_id,
            "name": self.name,
            "phone_number": self.phone_number
        }
        with open(file_name, 'w') as file:
            json.dump(partner_info, file, ensure_ascii=False, indent=4)


class Client(Partner):
    def __init__(self, partner_id, email, name, phone_number, is_company, gender=None, age=None, additional_info=None):
        super().__init__(partner_id, email, name, phone_number)
        self.is_company = is_company
        if not self.is_company:
            self.gender = gender
            self.age = age
            self.additional_info = additional_info if additional_info is not None else {}


    def get_orders(self, orders):
        # Возвращает все заказы клиента
        return [order for order in orders if order.client_id == self.partner_id]


class Supplier(Partner):
    def __init__(self, partner_id, email, name, phone_number):
        super().__init__(partner_id, email, name, phone_number)

    def get_deliveries(self, orders):
        # Возвращает все поставки поставщика
        return [order for order in orders if order.supplier_id == self.partner_id]
