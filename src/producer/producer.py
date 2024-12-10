import os
import time
from datetime import datetime, timezone
from kafka import KafkaProducer


def main():
    # Load Kafka configuration from environment variables
    broker = os.getenv("KAFKA_BROKER", "localhost:9092")
    topic = os.getenv("KAFKA_TOPIC", "test-topic")
    sasl_username = os.getenv("SASL_USERNAME", "user1")
    sasl_password = os.getenv("SASL_PASSWORD", "GrS1vePuhJ")
    sasl_mechanism = os.getenv("SASL_MECHANISM", "SCRAM-SHA-256")

    # Create Kafka producer with SASL authentication
    producer = KafkaProducer(
        bootstrap_servers=broker,
        sasl_mechanism=sasl_mechanism,
        security_protocol="SASL_PLAINTEXT",
        sasl_plain_username=sasl_username,
        sasl_plain_password=sasl_password
    )

    i = 0
    while True:
        timestamp = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

        message = f"Test message {i} | Timestamp: {timestamp}"

        producer.send(topic, value=message.encode('utf-8'))
        print(f"Sent: {message}")

        i += 1
        time.sleep(5)


if __name__ == "__main__":
    main()
