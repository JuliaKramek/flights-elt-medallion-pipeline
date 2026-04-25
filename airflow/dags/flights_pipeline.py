from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "Julia",
    "depends_on_past": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

PG = 'PGPASSWORD=airflow psql -h postgres -U airflow -d flights -f'

with DAG(
    dag_id="flights_pipeline",
    start_date=datetime(2026, 4, 20),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    description="ELT Medallion Pipeline for airline transactions",
    tags=["elt", "medallion", "postgres"],
) as dag:

    bronze_create_schema = BashOperator(
        task_id="bronze_create_schema",
        bash_command=f"{PG} /opt/project/bronze/create_schema.sql"
    )

    bronze_create_tables = BashOperator(
        task_id="bronze_create_tables",
        bash_command=f"{PG} /opt/project/bronze/create_tables.sql"
    )

    bronze_load_bronze = BashOperator(
        task_id="bronze_load_bronze",
        bash_command=f"{PG} /opt/project/bronze/load_bronze.sql"
    )

    silver_create_schema = BashOperator(
        task_id="silver_create_schema",
        bash_command=f"{PG} /opt/project/silver/create_schema.sql"
    )

    silver_create_tables = BashOperator(
        task_id="silver_create_tables",
        bash_command=f"{PG} /opt/project/silver/create_tables.sql"
    )

    silver_load = BashOperator(
        task_id="silver_load",
        bash_command=f"{PG} /opt/project/silver/load_silver.sql"
    )

    gold_create_schema = BashOperator(
        task_id="gold_create_schema",
        bash_command=f"{PG} /opt/project/gold/create_schema.sql"
    )

    gold_create_tables = BashOperator(
        task_id="gold_create_tables",
        bash_command=f"{PG} /opt/project/gold/create_tables.sql"
    )

    (
        bronze_create_schema
        >> bronze_create_tables
        >> bronze_load_bronze
        >> silver_create_schema
        >> silver_create_tables
        >> silver_load
        >> gold_create_schema
        >> gold_create_tables
    )
