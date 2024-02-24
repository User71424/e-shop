import json


class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name

    def save_to_json(self, file_name):
        product_info = {
            "product_id": self.product_id,
            "name": self.name
        }
        with open(file_name, 'w') as file:
            json.dump(product_info, file, ensure_ascii=False, indent=4)

    def get_all_orders(self, orders):
        """
        Возвращает список заказов, в которых присутствует данный продукт.
        """
        return [order for order in orders if self.product_id in [product.product_id for product in order.products]]
