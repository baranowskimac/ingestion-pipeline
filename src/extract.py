import requests

url = "https://api.nbp.pl/api/exchangerates/tables/A"

def fetch_rates():
    response = requests.get(url)
    data = response.json()
    print(data)


if __name__ == "__main__":
    fetch_rates()