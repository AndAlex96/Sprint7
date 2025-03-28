import pytest
import requests
import random
import string
import allure

class TestCreatingCourier:
    @allure.title('Проверка создания курьера')
    def test_creating_a_courier(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'password': password, 'firstName': first_name}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title('Проверка невозможности создания идентичного курьера')
    def test_can_not_create_two_identical_couriers(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'password': password, 'firstName': first_name}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 409

    @allure.title('Проверка невозможности создания курьера без логина')
    def test_error_create_couriers_without_login(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'password': password, 'firstName': first_name}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 400

    @allure.title('Проверка невозможности создания курьера без пароля')
    def test_error_create_couriers_without_password(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'firstName': first_name}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)
        assert response.status_code == 400

    @allure.title('Проверка невозможности создания курьера с уже существующим логином')
    def test_error_create_couriers_with_created_login(self, register_new_courier_and_return_login_password):
        login, password, first_name = register_new_courier_and_return_login_password
        payload = {'login': login, 'password': password, 'firstName': first_name}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # генерируем новые пароль и имя курьера, а логин оставляем старый
        password2 = generate_random_string(10)
        first_name2 = generate_random_string(10)

        payload2 = {'login': login, 'password': password2, 'firstName': first_name2}
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload2)

        assert response.status_code == 409

