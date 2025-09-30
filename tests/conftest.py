import allure
import pytest
import requests
from config.settings import API, URL
from utils.api_client import create_user_data, delete_user_by_auth_token


@pytest.fixture
def registered_user():
    payload = create_user_data()
    with allure.step("Регистрация нового пользователя"):
        r = requests.post(f'{URL.MAIN_URL}{API.CREATE_USER}', data=payload)
        response_data = r.json()
    yield {'response': r, 'data': response_data, 'payload': payload}
    auth_token = response_data.get('accessToken')
    if auth_token:
        with allure.step("Удаление созданного пользователя"):
            delete_user_by_auth_token(auth_token)
