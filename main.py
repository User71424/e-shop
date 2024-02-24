from models import Client, Supplier, Order, Product, Manager
import os

def main():
    # Предполагаем, что у нас есть директория для сохранения данных
    if not os.path.exists('data'):
        os.mkdir('data')

    # Создаем клиентов
    client1 = Client(partner_id="101", name="Иванов Иван", email="ivanov@example.com", phone_number="1234567890",
                     is_company=False, gender="мужской", age=30)
    client2 = Client(partner_id="1001", name="ООО 'Рога и Копыта'", email="petrov@example.com",
                     phone_number="0987654321", is_company=True)

    # Создаем поставщиков
    supplier1 = Supplier(partner_id="1002", name="Завод 'Прометей'", email="prometey@example.com", phone_number="1122334455")

    # Создаем товары
    product1 = Product(product_id="10001", name="Компьютер")
    product2 = Product(product_id="10034", name="Мышь")

    # Создаем заказы
    order1 = Order(order_id=1, client_id=client1.partner_id, supplier_id=supplier1.partner_id,
                   items=[product1.product_id], manager_id=None)
    order2 = Order(order_id=2, client_id=client2.partner_id, supplier_id=supplier1.partner_id,
                   items=[product1.product_id, product2.product_id],
                   manager_id=None, status="в обработке")

    # Создаем менеджеров
    manager1 = Manager(name="Сидоров Сидор", department="Отдел продаж")

    # Сохраняем информацию в JSON файлы
    client1.save_to_json('client1.json')
    client2.save_to_json('client1.json')
    supplier1.save_to_json('supplier1.json')
    product1.save_to_json('product1.json')
    product2.save_to_json('product2.json')
    order1.save_to_json('order1.json')
    order2.save_to_json('order2.json')
    manager1.save_to_json('manager1.json')


if __name__ == "__main__":
    main()
