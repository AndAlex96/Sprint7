import random
import string

def generate_random_string(length):
    #Генерирует случайную строку заданной длины, состоящую из букв нижнего регистра
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_login_password_name():
    #Генерирует логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)
    return [login, password, first_name]