import allure
import pytest


@allure.story('Проверки параметра name')
class TestDoRegisterName:

    @allure.title('Проверка обязательного параметра name')
    def test_do_register_name(self, client, data):
        api_data = client.do_register(email=data['email'],
                                      name=data['name'],
                                      password=data['password'])
        with allure.step(f'Запрос отправлен. Проверяем, что отправленный name совпадает с тем,'
                         f' что вернулось в ответе'):
            assert api_data.json()['name'] == data['name'], \
                f'Неверный name в ответе, получен {api_data.json()["name"]}'

    @allure.title('Проверка ответа, запрос отправлен c уже зарегистрированным name')
    def test_do_register_double_name(self, client, data):
        api_data = client.do_register(email=data['email'],
                                      name="Машенька",
                                      password=data['password'])
        with allure.step(f'Проверяем ответ'):
            assert api_data.json() == {"type": "error", "message": " Текущее ФИО Машенька уже есть в базе"}, \
                f'Неверный email в ответе, получен {api_data.json()}'

    @allure.title('Проверка ответа, запрос отправлен без обязательного параметра name')
    def test_do_register_no_name(self, client, data):
        api_data = client.do_register(email=data['email'],
                                      password=data['password'])
        with allure.step(f'Проверяем ответ'):
            assert api_data.json() == {"type": "error", "message": "Параметр name является обязательным!"}, \
                f'Неверный ответ, получен {api_data.json()}'

    @pytest.mark.xfail
    @allure.issue("Баг, можно зарегистрироваться с кривым name (вместо имени символы, должен быть фильтр)")
    @allure.title('Проверка ответа, запрос отправлен c некорректным параметром name (отправлены символы)')
    def test_do_register_invalid_name(self, client, data):
        api_data = client.do_register(email=data['email'],
                                      name='.....',
                                      password=data['password'])
        with allure.step(f'Проверяем ответ'):
            assert api_data.json() == {"type": "error", "message": "Некоректный name ....."}, \
                f'Неверный ответ, получен {api_data.json()}'
