import requests
from app.helpers.generate_random_string import generate_login_password_name
import pytest

from app.urls import BASE_URL


# создаем курьера
@pytest.fixture
def register_new_courier_and_return_login_password():
    # Генерируем логин, пароль и имя курьера
    return generate_login_password_name()


# получение ID курьера и его удаление из базы
@pytest.fixture
def delete_courier(login, password):

    yield

    payload = {'login':login, 'password':password}
    response = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)
    get_id = response.json()
    id_courier = get_id.get['id']
    response_del = requests.delete(f'{BASE_URL}/api/v1/courier/{id_courier}', data={'id':id_courier})

    assert response_del.status_code == 200