import allure
import pytest


@pytest.fixture(autouse=True)
def allure_mark_feature():
    allure.dynamic.label('feature', 'Создание новой компании')
