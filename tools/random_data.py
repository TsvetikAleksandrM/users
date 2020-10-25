import random
from string import ascii_lowercase
import numpy as np


class RndData:
    """
    Генератор рандомных данных
    """

    def rnd_email(self):
        """
        Генератор рандомного email
        """

        return ''.join(random.choice(ascii_lowercase) for i in range(20)) + "@gmail.com"

    def rnd_name(self):
        """
        Генератор рандомного имени
        """

        return ''.join(random.choice(ascii_lowercase) for i in range(20))

    def rnd_password(self, length=10):
        """
        Генератор рандомного email
        """
        digits = '0123456789'

        return ''.join(random.choice(digits) for _ in range(length))

    def rnd_array(self, number):
        """
        Генератор рандомного массива чисел, для параметра tasks и companies
        """
        return [np.random.randint(1, 99) for i in range(number)]

    def rnd_type(self):
        """
        Рандомный тип
        """
        return random.choice(['ИП', 'ООО', 'ОАО'])

    def all_registration_data(self):
        """
        Получение рандомных данных для регистрации
        """
        email = self.rnd_email()
        name = self.rnd_name()
        password = self.rnd_password()
        return {'email': email, 'name': name, 'password': password}

    def all_data_create_user(self):
        """
        Получение рандомных данных для создания пользователя
        """
        email = self.rnd_email()
        name = self.rnd_name()
        tasks = self.rnd_array(5)
        companies = self.rnd_array(3)
        return {'email': email, 'name': name, 'tasks': tasks, 'companies': companies}

    def all_data_create_company(self):
        """
        Получение рандомных данных для создания компании
        """
        company_name = self.rnd_name()
        company_type = self.rnd_type()
        return {'company_name': company_name, 'company_type': company_type}
