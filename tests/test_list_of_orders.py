import pytest
import requests
import allure
from app.urls import BASE_URL

@allure.title('Тест возвращения списка заказа')
class TestListOrders:
    @allure.step('Проверка возвращения списка заказов в теле ответа')
    @pytest.mark.parametrize("limit, page", [(10, 0)])
    def test_response_body_returns_a_list_of_orders(self, limit, page):
        response = requests.get(f'{BASE_URL}/api/v1/orders?limit={limit}&page={page}')

        assert response.status_code == 200

        response_data = response.json()
        assert 'orders' in response_data
        assert isinstance(response_data['orders'], list)

        # также проверяем, что количество заказов соответствует ожидаемому
        # <=, а не ==, т.к. заказов может быть свободных меньше, чем 10 в системе
        assert len(response_data['orders']) <= limit

