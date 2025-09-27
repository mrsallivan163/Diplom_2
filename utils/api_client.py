import requests
from faker import Faker
from config.settings import URL,API

def create_user_data():
    fake = Faker()
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()}
    return user_data

def register_new_user_and_return_credentials():
    payload = create_user_data()
    r = requests.post(f'{URL.MAIN_URL}{API.CREATE_USER}', payload)
    data = r.json()
    return {
        'email': data['user']['email'],
        'password': payload['password'],
        'name': data['user']['name'],
        'auth_token': data['accessToken']
    }

def delete_user_by_auth_token(auth_token):
    requests.delete(f'{URL.MAIN_URL}{API.DELETE_USER}', headers={'Authorization': f'{auth_token}'})
