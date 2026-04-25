import json
from kafka import KafkaConsumer
import psycopg2

# --- CONFIG ---
KAFKA_TOPIC = "flights_topic"
KAFKA_SERVER = "localhost:9093"

POSTGRES_CONFIG = {
    "host": "localhost",
    "port": "5433",
    "database": "flights",
    "user": "airflow",
    "password": "airflow"
}

MAX_MESSAGES = 100  

# --- CONNECT TO DB ---
conn = psycopg2.connect(**POSTGRES_CONFIG)
cursor = conn.cursor()

# --- CONNECT TO KAFKA ---
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

print(" Consumer started...")

# --- CONSUME ---
for i, message in enumerate(consumer):
    try:
        data = message.value

        cursor.execute("""
            INSERT INTO bronze.travel_raw (
                transaction_key,
                ticketing_airline,
                marketing_airline,
                agency,
                issue_date,
                departure_date,
                origin,
                destination,
                country,
                cabin
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data.get("TRANSACTION_KEY"),
            data.get("TICKETING_AIRLINE"),
            data.get("MARKETING_AIRLINE"),
            data.get("AGENCY"),
            data.get("ISSUE_DATE"),
            data.get("DEPARTURE_DATE"),
            data.get("ORIGIN"),
            data.get("DESTINATION"),
            data.get("COUNTRY"),
            data.get("CABIN")
        ))

        conn.commit()

        print(f"Inserted: {data.get('TRANSACTION_KEY')}")

    except Exception as e:
        print(f" Error: {e}")

    # STOP dla Airflow
    if i >= MAX_MESSAGES:
        print("Reached limit, stopping consumer...")
        break

# --- CLEANUP ---
cursor.close()
conn.close()
consumer.close()

print(" Consumer finished.")
