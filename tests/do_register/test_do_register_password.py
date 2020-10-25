import allure
import pytest


@allure.story('Проверки параметра password')
class TestDoRegisterPassword:

    @allure.title('Проверка ответа, запрос отправлен без обязательного параметра password')
    def test_do_register_no_password(self, client, data):
        api_data = client.do_register(email=data['email'],
                                      name=data['name'])
        with allure.step(f"Проверяем ответ"):
            assert api_data.json() == {'type': 'error', 'message': 'Параметр password является обязательным!'}, \
                f"Неверный ответ, получен {api_data.json()}"

    @pytest.mark.xfail
    @allure.issue("Баг, можно зарегистрироваться с кривым password (вместо пароля символы, должен быть фильтр)")
    @allure.title('Проверка ответа, запрос отправлен c некорректным параметром name (отправлены символы)')
    def test_do_register_invalid_password(self, client, data):
        api_data = client.do_register(email=data['email'],
                                      name=data['password'],
                                      password='.....')
        with allure.step(f'Проверяем ответ'):
            assert api_data.json() == {"type": "error", "message": "Некоректный password ....."}, \
                f"Неверный ответ, получен {api_data.json()}"
