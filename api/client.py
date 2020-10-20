import requests
import allure


class Client:
    """
    Запросы regress
    """

    def __init__(self, base_address):
        self.base_address = base_address

    def do_register(self, **kwargs):
        with allure.step(f'Регистрация на ресурсе: {self.base_address}'):
            return requests.post(url=f'{self.base_address}tasks/rest/doregister', data=kwargs)
