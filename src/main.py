import tomodachi
from aiokafka.errors import KafkaError, KafkaTimeoutError

from src.services.kafka import get_kafka_producer


@tomodachi.service
class Service(tomodachi.Service):
    name = 'kafka_tomodachi'

    options = {
        'http': {
            'port': 8080
        }
    }

    @tomodachi.http('GET', r'/send')
    async def kafka_endpoint(self, request):
        producer = await get_kafka_producer()
        try:
            await producer.send_and_wait(topic='topic_name', value='some message'.encode())
        except KafkaTimeoutError:
            return "produce timeout... maybe we want to resend data again?"
        except KafkaError as err:
            return "some kafka error on produce: {}".format(err)
        finally:
            await producer.stop()

        return True
