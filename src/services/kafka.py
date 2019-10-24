import asyncio

from aiokafka import (
    AIOKafkaProducer,
    AIOKafkaConsumer,
)

from src import settings


async def get_kafka_producer():
    producer = AIOKafkaProducer(
        bootstrap_servers=f'{settings.KAFKA_HOST_NAME}:{settings.KAFKA_HOST_PORT}',
        loop=asyncio.get_event_loop()
    )
    await producer.start()

    return producer


async def get_kafka_consumer():
    consumer = AIOKafkaConsumer(
        bootstrap_servers=f'{settings.KAFKA_HOST_NAME}:{settings.KAFKA_HOST_PORT}',
        loop=asyncio.get_event_loop()
    )
    await consumer.start()

    return consumer
