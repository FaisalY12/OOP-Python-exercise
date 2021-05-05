import requests

# URL = f'https://api.github.com/users/{name}/repos'

def fetch_repos(name):
    
    req = requests.get(f'https://api.github.com/users/{name}/repos')
    data = req.json():
    return data