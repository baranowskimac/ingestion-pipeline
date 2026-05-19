from google.cloud import bigquery
import pandas as pd

def load_to_bigquery(df):
    client = bigquery.Client(project="meb-dataportfolio-work")
    
    client.create_dataset("nbp_rates", exists_ok=True)
    
    table_id = "meb-dataportfolio-work.nbp_rates.exchange_rates"

    pandas_df  = df.to_pandas()

    job = client.load_table_from_dataframe(pandas_df , table_id)
    job.result()

    print(f"Loaded {len(pandas_df)} rows to {table_id}")