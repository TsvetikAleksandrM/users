import pytest
from api.client import Client
from tools.random_data import RndData as rd


@pytest.fixture(scope="session")
def client():
    return Client(base_address="http://users.bugred.ru/")


@pytest.fixture()
def data():
    return rd().all_registration_data()


@pytest.fixture()
def data_user():
    return rd().all_data_create_user()
