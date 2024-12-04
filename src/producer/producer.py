import os
from kafka import KafkaProducer

broker = os.getenv("KAFKA_BROKER", "localhost:9092")
topic = os.getenv("KAFKA_TOPIC", "test-topic")

producer = KafkaProducer(bootstrap_servers=broker)

for i in range(10):
    message = f"Test message {i}"
    producer.send(topic, value=message.encode('utf-8'))
    print(f"Sent: {message}")
producer.flush()
