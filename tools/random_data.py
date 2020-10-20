import random
from string import ascii_lowercase


class RndData:
    """
    Генератор рандомных данных
    """

    def rnd_email(self):
        """
        Генератор рандомного email
        """

        return ''.join(random.choice(ascii_lowercase) for i in range(20)) + "z@gmail.com"

    def rnd_name(self):
        """
        Генератор рандомного имени
        """

        return ''.join(random.choice(ascii_lowercase) for i in range(20)) + "z"

    def rnd_password(self, length=10):
        """
        Генератор рандомного email
        """
        digits = '0123456789'

        return ''.join(random.choice(digits) for _ in range(length))

    def all_data(self):
        email = self.rnd_email()
        name = self.rnd_name()
        password = self.rnd_password()
        return {'email': email, 'name': name, 'password': password}

