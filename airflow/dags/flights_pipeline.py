from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="flights_pipeline",
    start_date=datetime(2026, 4, 20),
    schedule_interval=None,
    catchup=False
) as dag:

    bronze = BashOperator(
        task_id="bronze",
        bash_command="python /opt/project/orchestration/bronze.py"
    )

    silver = BashOperator(
        task_id="silver",
        bash_command="python /opt/project/orchestration/silver.py"
    )

    gold = BashOperator(
        task_id="gold",
        bash_command="python /opt/project/orchestration/gold.py"
    )

    bronze >> silver >> gold