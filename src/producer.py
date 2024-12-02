from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="kafka.default.svc.cluster.local:9092",  # Kafka service address in K8s
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

if __name__ == "__main__":
    topic = "demo-topic"
    for i in range(10):
        message = {"id": i, "message": f"Test message {i}"}
        producer.send(topic, value=message)
        print(f"Produced: {message}")
        time.sleep(1)  # Simulate message production delay
    producer.close()
