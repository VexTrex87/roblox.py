import requests

def get(url):
    r = requests.get(url)
    data = r.json()
    return data
