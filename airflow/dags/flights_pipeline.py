from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "Julia",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=2)
}

with DAG(
    dag_id="flights_pipeline",
    start_date=datetime(2026, 4, 20),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    description="ELT Medallion pipeline for airline transactions"
) as dag:

    bronze = BashOperator(
        task_id="bronze_layer",
        bash_command="python /opt/project/orchestration/bronze.py"
    )

    silver = BashOperator(
        task_id="silver_layer",
        bash_command="spark-submit /opt/project/silver/silver_job.py"
    )

    gold = BashOperator(
        task_id="gold_layer",
        bash_command="python /opt/project/orchestration/gold.py"
    )

    bronze >> silver >> gold
