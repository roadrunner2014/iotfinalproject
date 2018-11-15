#------------ Kafka test app --------------------
import threading
import logging
import time
import json

from kafka import KafkaConsumer, KafkaProducer


class Consumer():
    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='localhost:9092',
                                 auto_offset_reset='earliest',
                                 value_deserializer=lambda m: json.loads(m).decode('utf-8'))
        consumer.subscribe(['testtopic'])

        for message in consumer:
            print (message)


Consumer()

