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
    start_date=datetime(2024, 1, 1),  # 🔥 poprawione
    schedule_interval=None,           # 🔥 manual trigger (lepsze na demo)
    catchup=False,
    default_args=default_args,
    description="ELT Medallion Pipeline with Kafka streaming",
    tags=["elt", "medallion", "kafka"],
) as dag:

    # --- BRONZE ---
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

    # --- SILVER ---
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

    # --- GOLD ---
    gold_create_schema = BashOperator(
        task_id="gold_create_schema",
        bash_command=f"{PG} /opt/project/gold/create_schema.sql"
    )

    gold_create_tables = BashOperator(
        task_id="gold_create_tables",
        bash_command=f"{PG} /opt/project/gold/create_tables.sql"
    )

    # --- STREAMING (Kafka Consumer) ---
    start_streaming = BashOperator(
        task_id="start_streaming",
        bash_command="python /opt/project/streaming/consumer.py"
    )

    # --- PIPELINE FLOW ---
    (
        bronze_create_schema
        >> bronze_create_tables
        >> bronze_load_bronze
        >> silver_create_schema
        >> silver_create_tables
        >> silver_load
        >> gold_create_schema
        >> gold_create_tables
        >> start_streaming   
    )
