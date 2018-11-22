# iotfinalproject
# Python code for IoT class final project with producer depencies below
from numpy import random
import time
import json
import sys
import os
from confluent_kafka import Producer

# Consumer depencies below
import sys
import os
from confluent_kafka import Consumer, KafkaException, KafkaError

# To generate the random IoT device info use the container below run the commands below
docker pull roadrunner2014/ubuntu:kafka

# in containter bin/bash using CloudKarafka.com on topic 'teamorange'
source /home/ubuntu/iotfinalproject/CrydermanKafka.sh

python /home/ubuntu/iotfinalproject/iotproducer.py

# for consumer run which will create a iotdevicedata.txt file with the consumer output
python consumer.py

# Outputs iotdevicedata.txt file in /home/ubuntu/
