import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

TRANSFORMED_TABLE = "clean_transactions"
RAW_TABLE = "raw_transactions"

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
        conn.execute(text(f'TRUNCATE TABLE {TRANSFORMED_TABLE}'))
        conn.commit()

    print('Table cleared.')


def transform_data(engine):
    with engine.connect() as conn:
        with open('sql/transform.sql') as f:
            conn.execute(text(f.read()))
        conn.commit()
    print('Done!')


if __name__ == "__main__":
    engine = get_db_engine()
    try:
        truncate_table(engine)
        transform_data(engine)
    except Exception as ex:
        print("Data could not be loaded to the database!", ex)
    finally:
        engine.dispose()