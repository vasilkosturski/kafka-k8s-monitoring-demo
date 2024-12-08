import os
import time
from kafka import KafkaProducer

def main():
    broker = os.getenv("KAFKA_BROKER", "localhost:9092")
    topic = os.getenv("KAFKA_TOPIC", "test-topic")

    producer = KafkaProducer(bootstrap_servers=broker)

    i = 0
    while True:
        message = f"Test message {i}"
        producer.send(topic, value=message.encode('utf-8'))
        print(f"Sent: {message}")
        i += 1
        time.sleep(1)


if __name__ == "__main__":
    main()
