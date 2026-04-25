import csv
import json
import time
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9093',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = "flights_topic"

with open("data/travelverse-dataset.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for i, row in enumerate(reader):
        if i >= 20:
            break

        producer.send(topic_name, row)
        print("Sent:", row)
        time.sleep(1)

producer.flush()
print("Done streaming.")