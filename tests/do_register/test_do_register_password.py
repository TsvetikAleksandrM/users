import allure
import pytest


class TestDoRegisterPassword:

    @allure.title('Проверка ответа, запрос отправлен без обязательного параметра password')
    def test_do_register_no_password(self, client, data):
        api_list_users = client.do_register(email=data['email'],
                                            name=data['name'])
        with allure.step(f"Проверяем ответ"):
            assert api_list_users.json() == {'type': 'error', 'message': 'Параметр password является обязательным!'}, \
                f"Неверный ответ, получен {api_list_users.json()}"

    @pytest.mark.xfail
    @allure.issue("Баг, можно зарегистрироваться с кривым password (вместо пароля символы, должен быть фильтр)")
    @allure.title('Проверка ответа, запрос отправлен c некорректным параметром name (отправлены символы)')
    def test_do_register_invalid_password(self, client, data):
        api_list_users = client.do_register(email=data['email'],
                                            name=data['password'],
                                            password='.....')
        with allure.step(f'Проверяем ответ'):
            assert api_list_users.json() == {"type": "error", "message": "Некоректный password ....."}, \
                f"Неверный ответ, получен {api_list_users.json()}"
