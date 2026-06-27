
#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from tqdm.auto import tqdm
from sqlalchemy import create_engine
import click


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='yellow_taxi_data', help='Target table name')
 
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):

    url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv'

    engine = create_engine(f'postgresql+psycopg://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    df = pd.read_csv(
        url
    )
    df.columns = df.columns.str.lower()


    df.head(0).to_sql(
                target_table, 
                con=engine, 
                if_exists="replace",
                index=False
            )
    print("Table created")
    
    df.to_sql(
        target_table , 
        con=engine, 
        if_exists="append",
        index=False)


if __name__ == '__main__':
    run()
