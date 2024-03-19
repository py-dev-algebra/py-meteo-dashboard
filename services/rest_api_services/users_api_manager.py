import requests
import random


def get_all_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()

    for user in users:
        user['avatar'] = f'https://robohash.org/{random.randint(1, 200)}?set=set3'
    
    return users


def get_user(id: int):
    response = requests.get(f'https://jsonplaceholder.typicode.com/users/{id}')
    user = response.json()
    user['avatar'] = f'https://robohash.org/{random.randint(1, 200)}?set=set3'
    
    return user