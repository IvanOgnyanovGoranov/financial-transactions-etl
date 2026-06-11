import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

def get_db_engine():
    load_dotenv()

    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')

    engine = create_engine(f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")

    return engine


def truncate_table(engine, table_name):
    with engine.connect() as conn:
        with open(f'sql/truncate_{table_name}.sql') as f:
            conn.execute(text(f.read()))
        conn.commit()
    print(f'{table_name} cleared.')
