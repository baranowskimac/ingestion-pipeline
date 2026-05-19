from src.extract import fetch_rates
from src.transform import transform_rates
from  src.load import load_to_bigquery

if __name__ == "__main__":
    url = "https://api.nbp.pl/api/exchangerates/tables/A"
    raw = fetch_rates(url)
    df = transform_rates(raw)
    load_to_bigquery(df)