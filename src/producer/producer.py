import os
import time
from datetime import datetime, timezone
from kafka import KafkaProducer


def main():
    broker = os.getenv("KAFKA_BROKER")
    topic = os.getenv("KAFKA_TOPIC")
    sasl_username = os.getenv("SASL_USERNAME")
    sasl_password = os.getenv("SASL_PASSWORD")
    sasl_mechanism = os.getenv("SASL_MECHANISM")

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
