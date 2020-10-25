import allure
import pytest


@allure.story('Проверки параметра email')
class TestDoRegisterEmail:

    @allure.title('Проверка обязательного параметра email')
    def test_do_register_email(self, client, data):
        api_data = client.do_register(email=data['email'],
                                      name=data['name'],
                                      password=data['password'])
        with allure.step(f'Запрос отправлен. Проверяем, что отправленный email совпадает с тем,'
                         f' что вернулось в ответе'):
            assert api_data.json()['email'] == data['email'], \
                f"Неверный email в ответе, получен {api_data.json()['email']}"

    @allure.title('Проверка ответа, запрос отправлен c уже зарегистрированным email')
    def test_do_register_double_email(self, client, data):
        api_data = client.do_register(email="milli@mail.ru",
                                      name=data['name'],
                                      password=data['password'])
        with allure.step(f'Проверяем ответ'):
            assert api_data.json() == {"type": "error", "message": " email milli@mail.ru уже есть в базе"}, \
                f"Неверный email в ответе, получен {api_data.json()}"

    @allure.title('Проверка ответа, запрос отправлен без обязательного параметра email')
    def test_do_register_no_email(self, client, data):
        api_data = client.do_register(name=data['name'],
                                      password=data['password'])
        with allure.step(f'Проверяем ответ'):
            assert api_data.json() == {'type': 'error', 'message': 'Параметр email является обязательным!'}, \
                f"Неверный ответ, получен {api_data.json()}"

    @pytest.mark.xfail
    @allure.issue("Баг, можно зарегистрироваться с кривым email (битый домен)")
    @allure.title('Проверка ответа, запрос отправлен c некорректным параметром email')
    def test_do_register_invalid_email(self, client, data):
        api_data = client.do_register(email=data['email'][:-1],
                                      name=data['name'],
                                      password=data['password'])
        with allure.step(f'Проверяем ответ'):
            assert api_data.json() == {"type": "error",
                                       "message": "Некоректный email hmrzavrxdsfxilqhrz@gmail.co"}, \
                f"Неверный email в ответе, получен {api_data.json()}"
