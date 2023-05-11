from confluent_kafka.avro import AvroProducer
from confluent_kafka import avro


def acked(err, msg):
    if err is not None:
        print('Failed to deliver message: %s: %s' % msg.value().decode('utf-8'), str(err))
    else:
        print('Message produced: %s' % msg.value().decode('utf-8'))


def kafka_m_producer(topic):
    producer_config = {
        'bootstrap.servers': 'localhost:9092',
        'schema.registry.url': 'http://localhost:8081', 
        'broker.address.family': 'v4'
    }
    #TODO 1.0: Cargar datos de schema avro.
    return None
