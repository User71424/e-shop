import json
from datetime import datetime


class Order:
    def __init__(self, order_id, client_id, supplier_id, manager_id, status="новый", items=None, created_at=None):
        self.order_id = order_id
        self.client_id = client_id
        self.supplier_id = supplier_id
        self.manager_id = manager_id
        self.status = status
        self.items = items if items is not None else []
        self.created_at = created_at if created_at is not None else datetime.now()

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        self.items = [item for item in self.items if item['item_id'] != item_id]

    def save_to_json(self, file_name):
        order_info = {
            "order_id": self.order_id,
            "client_id": self.client_id,
            "supplier_id": self.supplier_id,
            "manager_id": self.manager_id,  # Сохранение ID менеджера в JSON
            "items": self.items,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }
        with open(file_name, 'w') as file:
            json.dump(order_info, file, ensure_ascii=False, indent=4)

    def update_order_status(self, new_status):
        self.status = new_status

    def get_order_details(self):
        return {
            "order_id": self.order_id,
            "client_id": self.client_id,
            "supplier_id": self.supplier_id,
            "manager_id": self.manager_id,  # Включение ID менеджера в детали заказа
            "items": self.items,
            "created_at": self.created_at
        }
