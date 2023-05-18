from faust import Record
from fastavro import parse_schema

class Toot(Record):
    _schema = None

class Message(Record):
    timestamp: float
