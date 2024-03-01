import json
from datetime import datetime


class Order:
    def __init__(self, order_id, client_id, supplier_id, manager_id, status="новый", items=None, created_at=None):
        self.order_id = order_id
        self.client_id = client_id
        self.supplier_id = supplier_id
        self.manager_id = manager_id
        self.status = status
        self.items = items if items is not None else items[0]["item"]  # Список кортежей (item, price, quantity)
        self.created_at = created_at  # if created_at is not None else datetime.now()

    def add_item(self, item, price, quantity):
        """Добавляет товар в заказ со стоимостью и количеством."""
        self.items.append((item, price, quantity))

    def remove_item(self, item):
        """Удаляет товар из заказа по названию."""
        self.items = [i for i in self.items if i[0] != item]

    def get_details(self):
        return {
            "order_id": self.order_id,
            "client_id": self.client_id,
            "supplier_id": self.supplier_id,
            "manager_id": self.manager_id,
            "status": self.status,
            "items": self.items,
            "created_at": self.created_at
        }

    def update_order_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return str(self.get_details())

    def __repr__(self):
        return f'Order({self.order_id}, {self.client_id}, {self.supplier_id}, {self.manager_id}, {self.status!r},' \
               f' {self.items, self.created_at})'
