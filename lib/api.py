import requests
from .repository import Repository

# URL = f'https://api.github.com/users/{name}/repos'

def fetch_repos(name):
    req = requests.get(f'https://api.github.com/users/{name}/repos')
    for data in req.json():
        Repository(data)
        print(list(data))
    return data

