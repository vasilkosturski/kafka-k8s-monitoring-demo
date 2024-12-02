from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "demo-topic",
    bootstrap_servers="kafka.default.svc.cluster.local:9092",
    value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="demo-group",
)

if __name__ == "__main__":
    print("Starting Consumer...")
    for message in consumer:
        print(f"Consumed: {message.value}")
