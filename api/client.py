import requests
import allure
from requests.auth import HTTPBasicAuth


class Client:
    """
    Запросы regress
    """

    def __init__(self, base_address):
        self.base_address = base_address

    def do_register(self, **kwargs):
        with allure.step(f'Регистрация на ресурсе: {self.base_address}'):
            return requests.post(url=f'{self.base_address}tasks/rest/doregister', data=kwargs)

    def create_user(self, auth_user_name, auth_password, **kwargs):
        with allure.step(f'Создание нового пользователя'):
            return requests.post(url=f'{self.base_address}tasks/rest/createuser', data=kwargs,
                                 auth=HTTPBasicAuth(auth_user_name, auth_password))

    def create_company(self, auth_user_name, auth_password, **kwargs):
        with allure.step(f'Создание новой компании'):
            return requests.post(url=f'{self.base_address}tasks/rest/createcompany', data=kwargs,
                                 auth=HTTPBasicAuth(auth_user_name, auth_password))
