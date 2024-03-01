import json


class Partner:
    def __init__(self, partner_id, email, name, phone_number):
        self.partner_id = partner_id
        self.email = email
        self.name = name
        self.phone_number = phone_number

    def get_details(self):
        return {
            "partner_id": self.partner_id,
            "name": self.name,
            "phone_number": self.phone_number
        }

    def __str__(self):
        return str(self.get_details())

    def __repr__(self):
        return f'Partner({self.partner_id}, {self.email!r}, {self.name!r}, {self.phone_number})'


class Client(Partner):
    def __init__(self, partner_id, email, name, phone_number, is_company, gender=None, age=None, additional_info=None):
        super().__init__(partner_id, email, name, phone_number)
        self.is_company = is_company
        if not self.is_company:
            self.gender = gender
            self.age = age
            self.additional_info = additional_info if additional_info is not None else {}

    def get_details(self):
        partner_info = super().get_details()
        partner_info["is_company"] = self.is_company
        if not self.is_company:
            partner_info["gender"] = self.gender
            partner_info["age"] = self.age
            partner_info["additional_info"] = self.additional_info
        return partner_info

    def get_orders(self, orders):
        # Возвращает все заказы клиента
        return [order for order in orders if order.client_id == self.partner_id]

    def __repr__(self):
        if self.is_company:
            return f'Client({self.partner_id}, {self.email!r}, {self.name!r}, {self.phone_number}, {self.is_company})'
        else:
            return f'Client({self.partner_id}, {self.email!r}, {self.name!r}, {self.phone_number}, {self.is_company}, ' \
               f'{self.gender!r}, {self.age}, {self.additional_info})'


class Supplier(Partner):
    def __init__(self, partner_id, email, name, phone_number):
        super().__init__(partner_id, email, name, phone_number)

    def get_deliveries(self, orders):
        # Возвращает все поставки поставщика
        return [order for order in orders if order.supplier_id == self.partner_id]

    def __repr__(self):
        return f'Supplier({self.partner_id}, {self.email!r}, {self.name!r}, {self.phone_number})'
