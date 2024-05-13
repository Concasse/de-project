#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import time
import pyarrow.parquet as pq
from sqlalchemy import create_engine
import psycopg2
import argparse


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db  
    table_name = params.table_name
    url = params.url
    parquet_name = 'output.parquet'
    
    os.system(f'curl {url} -o {parquet_name}')

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df = pd.read_parquet(parquet_name)
    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    parquet_file = pq.ParquetFile(parquet_name)

    for batch_number, batch in enumerate(parquet_file.iter_batches(batch_size=100000)):
        t_start = time.time()
        
        batch_df = batch.to_pandas()
        
        batch_df['tpep_pickup_datetime'] = pd.to_datetime(batch_df['tpep_pickup_datetime'])
        batch_df['tpep_dropoff_datetime'] = pd.to_datetime(batch_df['tpep_dropoff_datetime'])

        batch_df.to_sql(name=table_name, con=engine, if_exists='append', index=False)

        
        t_end = time.time()
        
        print('Inserted chunk {} ..., took %.3f seconds'.format(batch_number) % (t_end - t_start))
    else:
        print("End of file reached. Ingest Data Done!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', help='username for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='host for postgres')
    parser.add_argument('--port', help='port for postgres')
    parser.add_argument('--db', help='database name for postgres')
    parser.add_argument('--table_name', help='name of table where we will write the results to')
    parser.add_argument('--url', help='url of the csv file')

    args = parser.parse_args()

    main(args)