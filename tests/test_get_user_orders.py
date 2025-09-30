import allure
import requests
from config.test_api_data import RESPONSE_TEXT
from config.test_api_data import TEST_DATA
from config.settings import API, URL


@allure.suite('Получение заказов пользователя')
class TestGetUserOrders:

    @allure.description("Проверка получения списка заказов пользователя, если он авторизован")
    @allure.title("Получение заказов пользователя(авторизован)")
    def  test_get_user_orders_if_auth(self, registered_user):
        headers = {'Authorization': registered_user['auth_token']}
        payload = TEST_DATA.VALID_INGREDIENTS
        r_create_order = requests.post(f"{URL.MAIN_URL}{API.CREATE_ORDER}", payload, headers=headers)
        r_get_order = requests.get(f"{URL.MAIN_URL}{API.GET_ORDERS}", headers=headers)
        assert r_get_order.status_code == 200
        assert r_get_order.json()['orders'][0]['number'] == r_create_order.json()['order']['number']


    @allure.description("Проверка получения списка заказов пользователя, если он НЕ авторизован")
    @allure.title("Получение заказов пользователя(не авторизован)")
    def test_get_user_orders_if_non_auth(self):
        r = requests.get(f"{URL.MAIN_URL}{API.GET_ORDERS}")
        assert r.status_code == 401
        assert r.json()['message'] == RESPONSE_TEXT.NON_AUTHORIZED