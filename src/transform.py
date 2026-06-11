from sqlalchemy import text
from src.utils import get_db_engine, truncate_table

TRANSFORMED_TABLE = "clean_transactions"
RAW_TABLE = "raw_transactions"


def transform_data(engine):
    with engine.connect() as conn:
        with open('sql/transform.sql') as f:
            conn.execute(text(f.read()))
        conn.commit()
    print('Done!')


if __name__ == "__main__":
    engine = get_db_engine()
    try:
        truncate_table(engine, TRANSFORMED_TABLE)
        transform_data(engine)
    except Exception as ex:
        print("Data could not be loaded to the database!", ex)
    finally:
        engine.dispose()