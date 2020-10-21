# import allure
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
#         print(data_user['email'])
#         print(data_user['name'])
#         print(data_user['tasks'])
#         print(data_user['companies'])
