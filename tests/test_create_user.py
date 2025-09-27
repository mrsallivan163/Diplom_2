import pytest
import allure
import requests
from utils.api_client import create_user_data
from config.settings import API, URL
from config.test_api_data import RESPONSE_TEXT


@allure.suite('Создание пользователя')
class TestCreateUser():

    @allure.description('Создание нового пользователя')
    @allure.title('Создание нового пользователя в системе')
    def test_create_new_user_success_when_fill_all_fields(self):
        payload = create_user_data()
        r = requests.post(f'{URL.MAIN_URL}{API.CREATE_USER}', payload)
        assert r.status_code == 200
        assert r.json()['success'] == True

    @allure.description('При создании раннее зарегистрированного пользователя вернётся код ответа 403 Forbidden ')
    @allure.title('Создание пользователя ранее зарегистрированного в системе')
    def test_not_create_two_identical_user(self, registered_user):
        payload = {
            "email": registered_user["email"],
            "password": registered_user["password"],
            "name": registered_user["name"]
        }
        r = requests.post(f'{URL.MAIN_URL}{API.CREATE_USER}', payload)
        assert r.status_code == 403
        assert r.json()['message'] == RESPONSE_TEXT.LOGIN_USED

    @allure.description('При создании пользователя без передачи обязательного поля вернётся код ответа 403 Forbidden ')
    @allure.title('Создание пользователя без обязательного поля')
    @pytest.mark.parametrize(
        'payload', [
            {"email": "Vova123", "name": "Vovka"},
            {"password": "1234567", "name": "Vovka"},
            {"email": "Vova123", "password": "1234"}
        ]
    )
    def test_create_user_missing_required_field(self, payload):
        r = requests.post(f'{URL.MAIN_URL}{API.CREATE_USER}', payload)
        assert r.status_code == 403
        assert r.json()['message'] == RESPONSE_TEXT.MISSING_REQUIRED_FIELD
