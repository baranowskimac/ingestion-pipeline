import requests

def fetch_rates(url):
    response = requests.get(url)
    data = response.json()
    return data
