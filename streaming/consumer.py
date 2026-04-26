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

# --- CONNECT TO POSTGRES ---
conn = psycopg2.connect(**POSTGRES_CONFIG)
cur = conn.cursor()

# --- CONNECT TO KAFKA ---
consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_SERVER,
    auto_offset_reset="earliest",
    group_id="flights_group",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print(" Consumer started, waiting for messages...")

# --- CONSUME ---
for i, message in enumerate(consumer):
    data = message.value

    try:
        cur.execute("""
            INSERT INTO bronze.travel_raw (
                transaction_key,
                ticketing_airline,
                ticketing_airline_cd,
                agency,
                issue_date,
                country,
                transaction_type,
                trip_type,
                seg_number,
                marketing_airline,
                marketing_airline_cd,
                flight_number,
                cabin,
                origin,
                destination,
                departure_date
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data.get("TRANSACTION_KEY"),
            data.get("TICKETING_AIRLINE"),
            data.get("TICKETING_AIRLINE_CD"),
            data.get("AGENCY"),
            data.get("ISSUE_DATE"),
            data.get("COUNTRY"),
            data.get("TRANSACTION_TYPE"),
            data.get("TRIP_TYPE"),
            data.get("SEG_NUMBER"),
            data.get("MARKETING_AIRLINE"),
            data.get("MARKETING_AIRLINE_CD"),
            data.get("FLIGHT_NUMBER"),
            data.get("CABIN"),
            data.get("ORIGIN"),
            data.get("DESTINATION"),
            data.get("DEPARTURE_DATE")
        ))

        conn.commit()
        print(f"Inserted: {data.get('TRANSACTION_KEY')}")

    except Exception as e:
        print(f" Error: {e}")
        conn.rollback()

    #  STOP dla Airflow
    if i >= MAX_MESSAGES:
        print(" Reached message limit, stopping consumer...")
        break

# --- CLEANUP ---
cur.close()
conn.close()
consumer.close()

print("Consumer finished.")
