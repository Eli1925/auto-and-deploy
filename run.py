import pandas as pd
import os
import configparser

from pgdb import PGDatabase

script_path = os.path.abspath(__file__)
print(f"Путь до скрипта: {script_path}")

# Получить директорию, в которой находится скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Директория скрипта: {script_dir}")

config = configparser.ConfigParser()
config.read(os.path.join(script_dir, 'config.ini'))

DATABASE_CREDS = config['Database']

df = pd.DataFrame()
data_path = os.path.join(script_dir, 'data')
if os.path.exists(data_path):
    all_files = os.listdir(data_path)
    csv_files = [file for file in all_files if file.endswith('.csv')]
    all_dataframes = []
    
    for file in csv_files:
        file_path = os.path.join(data_path, file)
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