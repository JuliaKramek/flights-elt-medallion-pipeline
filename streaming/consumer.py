import json
from kafka import KafkaConsumer
import psycopg2

conn = psycopg2.connect(
    host="localhost",        # jeśli docker: "postgres"
    port="5433",             # jeśli docker: 5432
    database="flights",
    user="airflow",
    password="airflow"
)

cur = conn.cursor()

consumer = KafkaConsumer(
    'flights_topic',
    bootstrap_servers='localhost:9093',   # jeśli docker: 'kafka:9092'
    auto_offset_reset='earliest',
    group_id='flights_group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print("🚀 Consumer działa, czekam na dane...")

for message in consumer:
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
        print("✅ Inserted:", data.get("TRANSACTION_KEY"))

    except Exception as e:
        print("❌ Error:", e)
        conn.rollback()