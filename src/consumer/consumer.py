import os
from kafka import KafkaConsumer

broker = os.getenv("KAFKA_BROKER", "localhost:9092")
topic = os.getenv("KAFKA_TOPIC", "test-topic")

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=broker,
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

for message in consumer:
    print(f"Received: {message.value.decode('utf-8')}")
