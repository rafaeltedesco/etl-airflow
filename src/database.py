from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import MetaData
import os
from typing import Union

load_dotenv(".env")

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')

POSTGRES_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(POSTGRES_DATABASE_URL)


def get_files_ids_from_db() -> Union[list[str], list[None]]:

    table_name = 'revenues'    
    metadata = MetaData(bind=engine)
    metadata.reflect()

    if table_name in metadata.tables: 
            query = f"SELECT DISTINCT file_id FROM {table_name}"
            database_gd_ids = pd.read_sql_query(query, engine)
            return list(database_gd_ids['file_id'])

    return []