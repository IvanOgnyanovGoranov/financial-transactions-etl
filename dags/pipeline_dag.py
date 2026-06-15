from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="pipeline_dag",
    start_date=datetime(2026, 6, 15),
    schedule="@daily",
    catchup=False,
    default_args={"retries": 2},
) as dag:
    
    ingest = BashOperator(
        task_id="ingest",
        bash_command="python -m src.ingest"
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="python -m src.transform"
    )

    ingest >> transform