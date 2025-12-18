import pandas as pd
import os
import configparser

from pgdb import PGDatabase

config = configparser.ConfigParser()
config.read('config.ini')

DATABASE_CREDS = config['Database']

df = pd.DataFrame()
if os.path.exists('data'):
    all_files = os.listdir('data')
    csv_files = [file for file in all_files if file.endswith('.csv')]
    all_dataframes = []
    
    for file in csv_files:
        file_path = os.path.join('data', file)
        df = pd.read_csv(file_path)
        os.remove(file_path)
        all_dataframes.append(df)

            

database = PGDatabase(
    host=DATABASE_CREDS['HOST'],
    database=DATABASE_CREDS['DATABASE'],
    user=DATABASE_CREDS['USER'],
    password=DATABASE_CREDS['PASSWORD'],
)
for item in all_dataframes:
    for i, row in item.iterrows():
        query = f"insert into sales values ('{row['doc_id']}', '{row['item']}', '{row['category']}', {row['amount']}, {row['price']}, {row['discount']})"
        print(query)
        database.post(query)