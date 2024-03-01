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
    product1 = Product(product_id=10001, name="Компьютер")
    product2 = Product(product_id="10034", name="Мышь")

    # Создаем заказы
    order1 = Order(order_id=1, client_id=client1.partner_id, supplier_id=supplier1.partner_id,
                   items=[(product1, 65, 3)], manager_id=None)
    order2 = Order(order_id=2, client_id=client2.partner_id, supplier_id=supplier1.partner_id,
                   items=[(product1, 50.99, 2), (product2, 63.5, 4)],
                   manager_id=None, status="в обработке")

    # Создаем менеджеров
    manager1 = Manager(employee_id=100001, name="Сидоров Сидор", department="Отдел продаж")

    # Сохраняем информацию в JSON файлы
    print(order2)
    print([order1, order2])
    print(product1)
    print(client1)
    print(supplier1)
    print([client1, client2, supplier1])
    print(manager1)
    print([manager1, order2])


if __name__ == "__main__":
    main()
