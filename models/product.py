import json


class Product:
    def __init__(self, product_id, name):
        self.product_id = product_id
        self.name = name

    def get_details(self):
        return {
            "product_id": self.product_id,
            "name": self.name
        }

    def get_all_orders(self, orders):
        """
        Возвращает список заказов, в которых присутствует данный продукт.
        """
        return [order for order in orders if self.product_id in [product.product_id for product in order.products]]

    def __str__(self):
        return str(self.get_details())

    def __repr__(self):
        return f'Product({self.product_id}, {self.name!r})'
