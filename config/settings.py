class URL:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site/'

class API:
    CREATE_USER = '/api/auth/register'
    LOGIN_USER = '/api/auth/login'
    CHANGE_USER_DATA = '/api/auth/user'
    DELETE_USER = '/api/auth/user'
    CREATE_ORDER = '/api/orders'
    GET_ORDERS = '/api/orders'
    headers = {"Content-Type": "application/json"}