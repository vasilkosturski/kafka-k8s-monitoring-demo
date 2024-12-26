from kafka import KafkaConsumer
import os

def main():
    broker = os.getenv("KAFKA_BROKER")
    topic = os.getenv("KAFKA_TOPIC")
    sasl_username = os.getenv("SASL_USERNAME")
    sasl_password = os.getenv("SASL_PASSWORD")
    sasl_mechanism = os.getenv("SASL_MECHANISM")
    consumer_group = os.getenv("KAFKA_CONSUMER_GROUP")

    consumer = KafkaConsumer(
        topic,
        group_id=consumer_group,
        bootstrap_servers=broker,
        enable_auto_commit=True,
        sasl_mechanism=sasl_mechanism,
        security_protocol="SASL_PLAINTEXT",
        sasl_plain_username=sasl_username,
        sasl_plain_password=sasl_password
    )

    print(f"Consumer started in group '{consumer_group}' consuming topic '{topic}'")

    for message in consumer:
        print(f"Received: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    main()
