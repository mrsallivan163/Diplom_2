import allure
import pytest
import requests

from config.test_api_data import RESPONSE_TEXT
from utils.api_client import create_user_data
from config.settings import API, URL


@allure.suite('Изменение данных пользователя')
class TestChangeUserData:

    @pytest.mark.parametrize("field", ["name", "email", "password"])
    @allure.description("Авторизованный пользователь может успешно изменить значение своего {field}")
    @allure.title("Успешное изменение {field} авторизованного пользователя")
    def test_changing_user_data_if_user_auth(self, registered_user, field):
        new_value = create_user_data()[field]
        payload = {field: new_value}
        headers = {'Authorization': registered_user['auth_token']}
        r = requests.patch(f'{URL.MAIN_URL}{API.CHANGE_USER_DATA}', payload, headers=headers)
        assert r.status_code == 200
        assert r.json().get('success') is True
        if field in ['name', 'email']:
            assert r.json()['user'][field] == new_value

    @allure.description("Неавторизованный пользователь при изменении данных получает код ответа 401 Unauthorized.")
    @allure.title("Неуспешное изменение данных пользователя, если он не авторизован")
    def test_failed_changing_user_data_if_user_non_authorized(self):
        r = requests.patch(f"{URL.MAIN_URL}{API.CHANGE_USER_DATA}", create_user_data())
        assert r.status_code == 401
        assert r.json()['message'] == RESPONSE_TEXT.NON_AUTHORIZED
