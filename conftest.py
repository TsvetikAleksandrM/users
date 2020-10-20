import pytest
from api.client import Client
from tools.random_data import RndData as rd


@pytest.fixture(scope="session")
def client():
    return Client(base_address="http://users.bugred.ru/")


@pytest.fixture()
def data():
    data = rd().all_info()
    return data
