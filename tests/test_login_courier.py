import pytest
import requests
import allure
from app.urls import BASE_URL

@allure.title('Тест авторизации курьера')
class TestLoginCourier:
    @allure.step('Проверка авторизации курьера')
    def test_courier_is_login_passed(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'password': password, 'firstName': first_name}
        requests.post(f'{BASE_URL}/api/v1/courier', data=payload)
        payload_login_password = {'login': login, 'password': password}
        response_auth = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload_login_password)
        assert response_auth.status_code == 200
        assert 'id' in response_auth.json()

    @allure.step('Проверка появления ошибки при авторизации с неверным логином')
    def test_error_auth_with_incorrect_login(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'password': password, 'firstName': first_name}
        requests.post(f'{BASE_URL}/api/v1/courier', data=payload)
        incorrect_login = f'{login} + 123'
        new_payload = {'login': incorrect_login, 'password': password}
        response_auth = requests.post(f'{BASE_URL}/api/v1/courier/login', data=new_payload)
        assert response_auth.status_code == 404
        assert response_auth.json() == '"message": "Учетная запись не найдена"'

    @allure.step('Проверка появления ошибки при авторизации с неверным паролем')
    def test_error_auth_with_incorrect_password(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'password': password, 'firstName': first_name}
        requests.post(f'{BASE_URL}/api/v1/courier', data=payload)
        incorrect_password = f'{password} + 123'
        new_payload = {'login': login, 'password': incorrect_password}
        response_auth = requests.post(f'{BASE_URL}/api/v1/courier/login', data=new_payload)
        assert response_auth.status_code == 404
        assert response_auth.json() == '"message": "Учетная запись не найдена"'

    @allure.step('Проверка появления ошибки при авторизации без логина')
    def test_error_auth_without_login(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'password': password, 'firstName': first_name}
        requests.post(f'{BASE_URL}/api/v1/courier', data=payload)
        new_payload = {'password': password}
        response_auth = requests.post(f'{BASE_URL}/api/v1/courier/login', data=new_payload)
        assert response_auth.status_code == 400
        assert response_auth.json() == '"message":  "Недостаточно данных для входа"'

    @allure.step('Проверка появления ошибки при авторизации без пароля')
    def test_error_auth_without_password(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'password': password, 'firstName': first_name}
        requests.post(f'{BASE_URL}/api/v1/courier', data=payload)
        new_payload = {'login': login}
        response_auth = requests.post(f'{BASE_URL}/api/v1/courier/login', data=new_payload)
        assert response_auth.status_code == 400
        assert response_auth.json() == '"message":  "Недостаточно данных для входа"'

    @allure.step('Проверка появления ошибки при попытки авторизации с незарегистрированными данными')
    def test_try_auth_without_regisration(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'password': password}
        response_auth = requests.post(f'{BASE_URL}/api/v1/courier/login', data=payload)
        assert response_auth.status_code == 404
        assert response_auth.json() == '"message": "Учетная запись не найдена"'

        # не сделал изначально, т.к. в задании не было сказано это,
        # а в другом задании (регистрация курьера) было отмечено - проверить тело, подумал,
        # что раз там четко сформульрована задача, то и тут аналогично нужно было бы проверить,
        # если бы это было отдельно указано