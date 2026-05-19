import polars as pl

def transform_rates(raw):
    rates = raw[0]["rates"]
    df = pl.DataFrame(rates)
    df = df.with_columns(
            pl.lit(raw[0]["effectiveDate"]).alias("effective_date")
        )

    return df