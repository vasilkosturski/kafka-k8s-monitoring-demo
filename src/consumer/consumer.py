from kafka import KafkaConsumer
import os

def main():
    broker = os.getenv("KAFKA_BROKER", "localhost:9092")
    topic = os.getenv("KAFKA_TOPIC", "test-topic")
    sasl_username = os.getenv("SASL_USERNAME", "user1")
    sasl_password = os.getenv("SASL_PASSWORD", "GrS1vePuhJ")
    sasl_mechanism = os.getenv("SASL_MECHANISM", "SCRAM-SHA-256")

    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=broker,
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        sasl_mechanism=sasl_mechanism,
        security_protocol="SASL_PLAINTEXT",
        sasl_plain_username=sasl_username,
        sasl_plain_password=sasl_password
    )

    # Consume messages from the topic
    for message in consumer:
        print(f"Received: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    main()
