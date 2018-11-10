#-------- randomip.py ---------------------------------
from numpy import random
import time
from kafka import SimpleProducer, KafkaClient

# connect to Kafka broker
#kafka = KafkaClient('localhost:9092')
#kafka = KafkaClient('35.226.74.108:9092')
#producer = SimpleProducer(kafka)
# assign a topic
topic = 'test'



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


def sendiotdata(totaldevices):
	iotdevice = 1
	while iotdevice <= totaldevices:
		print("IoT device no."), iotdevice
		iotdeviceinfo = IoTdeviceScanData(randomip(1), openport(), stateport(), serviceport(openport()), portos(serviceport(openport())),os())
		#producer.send_messages(topic,iotdeviceinfo)
		iotdevice += 1
		print('')

totaliotdevices = int(raw_input("Enter total IoT devices: "))

# Send IoT device info to Kafka broker
sendiotdata(totaliotdevices)

