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

    def all_registration_data(self):
        email = self.rnd_email()
        name = self.rnd_name()
        password = self.rnd_password()
        return {'email': email, 'name': name, 'password': password}

    def all_data_create_user(self):
        email = self.rnd_email()
        name = self.rnd_name()
        tasks = self.rnd_array(5)
        companies = self.rnd_array(3)
        return {'email': email, 'name': name, 'tasks': tasks, 'companies': companies}