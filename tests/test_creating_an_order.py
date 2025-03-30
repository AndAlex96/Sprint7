import pytest
import requests
import allure
from app.urls import BASE_URL

@allure.title('Тест создания заказа')
class TestCreatingOrder:


    @pytest.mark.parametrize("color", [(["BLACK"]), (["GREY"]), (["BLACK", "GREY"]),([])])
    @allure.step(f'Проверка создания заказа c одним, двумя цветами и без выбора цвета')
    def test_creating_an_order_with_color(self,     color):
        payload = {
            "firstName": "Андрей",
            "lastName": "Плотников",
            "address": "Королева",
            "metroStation": 'Черкизовская',
            "phone": "88225866996",
            "rentTime": 5,
            "deliveryDate": "2026-06-06",
            "comment": "Жду заказ",
            "color": color
        }
        response = requests.post(f'{BASE_URL}/api/v1/orders', data=payload)

        assert response.status_code == 201
        assert 'track' in response.json()
