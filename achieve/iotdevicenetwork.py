# -------------------------- iotdevices.py --------------------------
# ssc.start()
# ssc.awaitTermination()
# spark-submit --jars spark-streaming-kafka-assembly_2.10-1.6.1.jar s.py localhost:9092 test

#    Spark
from pyspark import SparkConf, SparkContext
from operator import add
import sys
#    Spark Streaming
from pyspark.streaming import StreamingContext
#    Kafka
from pyspark.streaming.kafka import KafkaUtils
from kafka import SimpleProducer, KafkaClient
from kafka import KafkaProducer

import json
import ast

from datetime import datetime
import urllib3

from numpy import random
from time import sleep
#import pika

# 192.168.113.134 \n
# "Nmap scan report for 192.168.0.24" \n
# "PORT	STATE	SERVICE	REASON	VERSION" \n
# "22/tcp	open	ssh		syn-ack	SSH-2.0 OpenSSH 7.4p1 Raspbian-10deb9u4 " \n
# "5900/tcp	open	vnc		syn-ack	RealVNC Enterprise" \n
# "MAC Address: " \n
# "Running: Linux 2.4.X | 3.x " \n
# "OS CPE:  cpe:/o:linux:linux_kernel:2.4.37 cpe:/0:linux:linux_kernel:3.2"" \n
# "OS details: DD-WRT v24.sp2 (Linux 2.4.37), Linux 3.2 " \n

#Kafka connection details
producer = KafkaProducer(bootstrap_servers='35.226.74.108:9092')
kafkaStream = KafkaUtils.createStream(ssc, 'cdh57-01-node-01.moffatt.me:2181', 'spark-streaming', {'testdata':1})
parsed = kafkaStream.map(lambda v: json.loads(v[1]))

# Set Spark details
sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")

#-----IoT device info to send to kafka ---------
authors_dstream = parsed.map(lambda tweet: tweet['user']['screen_name'])
author_counts_sorted_dstream = author_counts.transform(\
  (lambda foo:foo\
   .sortBy(lambda x:( -x[1]))))
top_five_authors = author_counts_sorted_dstream.transform\
  (lambda rdd:sc.parallelize(rdd.take(5)))
top_five_authors.pprint()

def randomip(y):
    rand1 = str(y)
    rand2 = str()
    rand3 = str()
    rand4 = str()
    for x in range(2):
        rx = random.randint(0,9)
        rand1 += str(rx)
    for x in range(3):
         rx = random.randint(0, 9)
         rand2 += str(rx)
    for x in range(3):
         rx = random.randint(0, 9)
         rand3 += str(rx)
    for x in range(3):
         rx = random.randint(0, 9)
         rand4 += str(rx)
    randip = rand1 + '.' + rand2 + '.' + rand3 + '.' + rand4
    return randip

def openport():
    randport = str()
    op = random.randint(0,20)
    if op <= 2 or op > 14:
        randport = 'none'
    elif op > 2 and op <= 4:
        randport = '22'
    elif op > 4 and op <= 6:
        randport = '443'
    elif op > 6 and op <= 8:
        randport = '2185'
    elif op > 8 and op <= 10:
        randport = '80'
    elif op > 10 and op <= 12:
        randport = '20'
    elif op > 12 and op <= 14:
        randport = '25'
    return randport

def stateport():
    xx = random.randint(0,5)
    if xx < 4:
        statept = 'open'
    else:
        statept = 'closed'
    return statept


def serviceport(x):
    state = str()
    if x == '20':
        state = 'FTP'
    elif x == '22':
        state = 'ssh'
    elif x == '25':
        state = 'SMTP'
    elif x == '80':
        state = 'HTTP'
    elif x == '443':
        state = "HTTPS"
    elif x == '2185':
        state = 'FTP'
    elif x == 'none':
        state = 'none'
    return state

def portos(x):
    if x == 'ssh':
        opsys = 'OpenSSh 6.6'
    elif x == 'FTP':
        opsys = 'FileZilla 2018-07-23'
    elif x == 'SMTP':
        opsys = 'Linux 2.4.37'
    elif x == 'HTTP' or x == 'HTTPS':
        opsys = 'OpenSSL 1.0.2'
    else:
        opsys = 'Linux 3.4'
    return opsys

def os():
    yy = random.randint(0,9)
    sys = str()
    if yy <= 3:
        sys = 'Windows 7'
    if yy == 4 and yy <= 6:
        sys = 'Linux 3.2'
    if yy > 6 and yy <= 8:
        sys = 'Raspbian 10deb9u4'
    if yy == 9:
        sys = 'RealVNC Enterprise'
    return sys

class IoTdeviceScanData(object):
    def __init__(self, ip_addr, openports, portstate, portservice, portoperatingsystem, opertingsystem):
        print("Scanning IoT devices for vulnerabilities...")

        self.ip_addr = ip_addr
        self.openports = openports
        self.portstate = portstate
        self.portservice = portservice
        self.portoperatingsystem = portoperatingsystem
        self.opertingsystem = opertingsystem

        print("Initial IP Address: {}".format(self.ip_addr))
        print("Open ports: {}".format(self.openports))
        print("Port state: {}").format(self.portstate)
        print("Port protocol: {}".format(self.portservice))
        print("Port OS: {}").format(self.portoperatingsystem)
        print("Operating System: {}").format(self.opertingsystem)



iotdevice = IoTdeviceScanData(randomip(1), openport(), stateport(), serviceport(openport()), portos(serviceport(openport())),os())

def handler(message):
    records = message.collect()
    for record in records:
        producer.send('spark.out', str(record))
        producer.flush()

def main():
    sc = SparkContext(appName="PythonStreamingIoTdeviceInfo")
    ssc = StreamingContext(sc, 10)

    brokers, topic = sys.argv[1:]
    kvs = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": brokers})
    kvs.foreachRDD(handler)

    ssc.start()
    ssc.awaitTermination()
if __name__ == "__main__":

   main()

