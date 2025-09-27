import allure
import pytest
from utils.api_client import register_new_user_and_return_credentials, delete_user_by_auth_token


@pytest.fixture
def registered_user():
    with allure.step("Регистрация нового пользователя"):
        credentials = register_new_user_and_return_credentials()
    yield credentials
    with allure.step("Удаление созданного пользователя"):
        delete_user_by_auth_token(credentials['auth_token'])
