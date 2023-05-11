import csv
import json
from fastavro import parse_schema

def read_avro_schema():
    schema = {}
    with open("../config/avro/mastodon-topic-value.avsc") as file:
        schema = parse_schema(json.load(file))
    return schema
