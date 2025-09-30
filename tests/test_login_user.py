import allure
import requests
from config.settings import API, URL
from config.test_api_data import RESPONSE_TEXT, TEST_DATA

@allure.suite('Авторизация пользователя')
class TestLoginUser:

    @allure.description('Успешная авторизация пользователя')
    @allure.title('Авторизация пользователя с валидными данными')
    def test_login_user_success_when_with_valid_login_data(self, registered_user):
        payload = {
            "email": registered_user["email"],
            "password": registered_user["password"]
        }
        r = requests.post(f'{URL.MAIN_URL}{API.LOGIN_USER}', payload)
        assert r.status_code == 200
        assert r.json().get('success') == True

    @allure.description('При авторизации пользователя с невалидными данными - вернётся код ответа 401 Unauthorized')
    @allure.title('Неуспешная авторизация пользователя в системе')
    def test_login_user_failed_when_with_invalid_login_data(self):
        r = requests.post(f'{URL.MAIN_URL}{API.LOGIN_USER}', TEST_DATA.INVALID_LOGIN_DATA)
        assert r.status_code == 401
        assert r.json()['message'] == RESPONSE_TEXT.FAILED_LOGIN
