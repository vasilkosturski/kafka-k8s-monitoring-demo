from kafka import KafkaProducer
import os
import random
import time
from datetime import datetime


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

    event_types = ["INFO", "WARNING", "ERROR"]

    while True:
        event_type = random.choice(event_types)
        message = f"{event_type} | Event-{random.randint(1, 1000)} | {datetime.now().isoformat()}"

        producer.send(topic, value=message.encode('utf-8'))
        print(f"Produced: {message}")

        time.sleep(random.uniform(0.2, 1.5))


if __name__ == "__main__":
    main()
