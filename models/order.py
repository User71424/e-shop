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

    def save_to_json(self, file_name):
        order_info = {
            "order_id": self.order_id,
            "client_id": self.client_id,
            "supplier_id": self.supplier_id,
            "manager_id": self.manager_id,
            "status": self.status,
            "items": [{"item": item[0], "price": item[1], "quantity": item[2]} for item in self.items],
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
            "manager_id": self.manager_id,
            "status": self.status,
            "items": [{"item": item["item"], "price": item["price"], "quantity": item["quantity"]} for item \
                      in self.items],
            "created_at": self.created_at
        }
