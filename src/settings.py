import os

KAFKA_HOST_NAME: str = os.getenv('KAFKA_HOST_NAME', 'localhost')
KAFKA_HOST_PORT: int = os.getenv('KAFKA_HOST_NAME', 9092)
