import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

TABLE_NAME = "raw_transactions"
CSV_PATH = 'data/PS_20174392719_1491204439457_log.csv'
CHUNK_SIZE = 50000

def get_db_engine():
    load_dotenv()

    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

    return engine


def truncate_table(engine):
    with engine.connect() as conn:
        conn.execute(text(f'TRUNCATE TABLE {TABLE_NAME}'))
        conn.commit()

    print('Table cleared.')

def load_data(engine):
    total_rows = sum(1 for _ in open(CSV_PATH)) - 1
    total_chunks = (total_rows // CHUNK_SIZE) + 1   

    transactions_data_chunk = pd.read_csv(CSV_PATH, nrows=500000, chunksize=CHUNK_SIZE)

    for i, chunk in enumerate(transactions_data_chunk):
        print(f'Loading chunk {i + 1}/{total_chunks}')


        chunk.to_sql(
            name=TABLE_NAME,
            con=engine,
            if_exists='append',
            index=False
        )

    print('Done!')


if __name__ == "__main__":
    engine = get_db_engine()
    try:
        truncate_table(engine)
        load_data(engine)
    except Exception as ex:
        print("Data could not be loaded to the database!", ex)
    finally:
        engine.dispose()