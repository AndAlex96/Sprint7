import pytest
import requests
import allure

class TestListOrders:
    @allure.title('Проверка возвращения списка заказов в теле ответа')
    def test_response_body_returns_a_list_of_orders(self):

        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders?limit=10&page=0')

        if response.status_code == 200:
            response_data = response.json()

            # Проверяем, что в ответе есть ключ 'orders' и он является списком
            if 'orders' in response_data and isinstance(response_data['orders'], list):
                print(f"Получено {len(response_data['orders'])} заказов.")
                # Выводим информацию о заказах
                for order in response_data['orders']:
                    print(f"ID заказа: {order['id']}, Имя: {order['firstName']}, Фамилия: {order['lastName']}")
            else:
                print("Ключ 'orders' отсутствует или не является списком.")
        else:
            print(f"Ошибка при получении заказов: {response.status_code}")

