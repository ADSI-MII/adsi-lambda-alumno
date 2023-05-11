from aux.misc.utils import read_avro_schema
from faust import Record
from fastavro import parse_schema

class Toot(Record):
    _schema = read_avro_schema()

class Message(Record):
    timestamp: float