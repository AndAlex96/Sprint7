import requests
import random
import string
import pytest


# метод генерирует логин, пароль и имя и возвращает их
@pytest.fixture
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    login_pass.append(login)
    login_pass.append(password)
    login_pass.append(first_name)

    # возвращаем список
    return login_pass


# получение ID курьера и его удаление из базы
@pytest.fixture
def delete_courier(login, password):

    yield

    payload = {'login':login, 'password':password}
    response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)
    get_id = response.json()
    id_courier = get_id.get['id']
    response_del = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{id_courier}', data={'id':id_courier})

    assert response_del.status_code == 200