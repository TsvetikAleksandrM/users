# import allure
# import pytest
#
#
# class TestCreateUserEmail:
#
#     @allure.title('Проверка параметра email')
#     def test_create_user_email(self, client, data_user):
#         api_list_users = client.create_user(email=data_user['email'],
#                                             name=data_user['name'],
#                                             tasks=data_user['tasks'],
#                                             companies=data_user['companies']
#                                             )
#         print(api_list_users.json())
        # with allure.step(f"Запрос отправлен. Проверяем, что отправленный email совпадает с тем,"
        #                  f" что вернулось в ответе."):
        #     assert api_list_users.json()['email'] == data['email'], \
        #         f"Неверный email в ответе, получен {api_list_users.json()['email']}"