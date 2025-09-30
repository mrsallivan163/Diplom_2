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

def delete_user_by_auth_token(auth_token):
    requests.delete(f'{URL.MAIN_URL}{API.DELETE_USER}', headers={'Authorization': f'{auth_token}'})
