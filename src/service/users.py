import requests


def fetch_user(user_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    return response.json()
