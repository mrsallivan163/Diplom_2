import allure
import requests
from config.test_api_data import RESPONSE_TEXT
from config.test_api_data import TEST_DATA
from config.settings import API, URL


@allure.suite('Создание заказа ')
class TestChangeUserData():

    @allure.description('Проверка создания заказа с ингредиентами, если пользователь авторизован в системе')
    @allure.title('Создание заказа с ингредиентами под авторизованным пользователем')
    def test_create_order_is_auth(self, registered_user):
        headers = {'Authorization': registered_user['auth_token']}
        payload = TEST_DATA.VALID_INGREDIENTS
        r = requests.post(f'{URL.MAIN_URL}{API.CREATE_ORDER}', payload, headers=headers)
        assert r.status_code == 200
        assert r.json().get("success") is True

    #INFO: Тест упадет т.к. неавторизованному пользователю можно сделать заказ - это БАГ.
    # мы не должны давать оформлять пользователю обезличенные заказы
    @allure.description('Проверка создания заказа с ингредиентами, если пользователь НЕ авторизован в системе')
    @allure.title('Создание заказа с ингредиентами под неавторизованным пользователем')
    def test_create_order_is_non_auth(self):
        payload = TEST_DATA.VALID_INGREDIENTS
        r = requests.post(f'{URL.MAIN_URL}{API.CREATE_ORDER}', payload)
        assert r.status_code == 401
        assert r.json()['message'] == RESPONSE_TEXT.NON_AUTHORIZED

    @allure.description('Если не передать ни один ингредиент, вернётся код ответа 400 Bad Request')
    @allure.title('Создание заказа с ингредиентами под авторизованным пользователем')
    def test_create_order_is_auth_with_empty_list_ingredients(self, registered_user):
        headers = {'Authorization': registered_user['auth_token']}
        payload = TEST_DATA.EMPTY_LIST_INGREDIENTS
        r = requests.post(f'{URL.MAIN_URL}{API.CREATE_ORDER}', payload, headers=headers)
        assert r.status_code == 400
        assert r.json()['message'] == RESPONSE_TEXT.EMPTY_LIST_INGREDIENTS

    @allure.description('Если в запросе передан невалидный хеш ингредиента, вернётся код ответа 500Internal Server Error')
    @allure.title('Создание заказа с невалидным хэшом игрединета')
    def test_create_order_is_auth_with_invalid_hash_ingredient(self, registered_user):
        headers = {'Authorization': registered_user['auth_token']}
        payload = TEST_DATA.INVALID_INGREDIENTS
        r = requests.post(f'{URL.MAIN_URL}{API.CREATE_ORDER}', payload, headers=headers)
        assert r.status_code == 500
        assert 'Internal Server Error' in r.text
