import allure
import pytest


@allure.story('Проверки параметра company_name')
class TestCreateCompanyCompanyName:

    @pytest.mark.xfail
    @allure.issue("Баг, создание компании не проходит, не видит параметр company_users и email_owner")
    @allure.title('Проверка обязательного параметра company_name')
    def test_company_name(self, client, data, data_company):
        api_data_register = client.do_register(email=data['email'],
                                               name=data['name'],
                                               password=data['password'])

        api_data_company = client.create_company(company_name=data_company['company_name'],
                                                 company_type=data_company['company_type'],
                                                 company_users=[api_data_register.json()['email']],
                                                 email_owner=api_data_register.json()['email'],
                                                 auth_user_name=api_data_register.json()['email'],
                                                 auth_password=api_data_register.json()['password'])

        with allure.step(f'Запрос отправлен. Проверяем, что отправленный company_name совпадает с тем,'
                         f' что вернулось в ответе'):
            assert data_company['company_name'] == api_data_company.json()['company']['name'], \
                f"Неверный email в ответе, получен {api_data_company.json()}"
