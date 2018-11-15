#-------- randomiotinfo.py ---------------------------------
from numpy import random
import time



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
    op = random.randint(0,12)
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
    xx = random.randint(0,6)
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
    yy = random.randint(0,12)
    sys = str()
    if yy <= 3:
        sys = 'Windows 7'
    if yy == 4 and yy <= 6:
        sys = 'Linux 3.2'
    if yy > 6 and yy <= 8:
        sys = 'Raspbian 10deb9u4'
    if yy > 8 and yy <= 10:
        sys = 'RealVNC Enterprise'
    if yy > 10 and yy <= 12:
        sys = 'FreeRTOS v10.1.1'
    return sys

def iottemp():
    return str(random.randint(0,99))

def iotcpu():
    return str(random.randint(1,99))

def iotmem():
    return str(random.randint(1,99))


class IoTdeviceScanData(object):
    def __init__(self, ip_addr, openports, portstate, portservice, portoperatingsystem, operatingsystem,iottemp,iotcpu,iotmem):
        print("Scanning IoT devices for vulnerabilities...")

        self.ip_addr = ip_addr
        self.openports = openports
        self.portstate = portstate
        self.portservice = portservice
        self.portoperatingsystem = portoperatingsystem
        self.operatingsystem = operatingsystem
        self.iottemp = iottemp
        self.iotcpu = iotcpu
        self.iotmem = iotmem

        print("Initial IP Address: {}".format(self.ip_addr))
        print("Open ports: {}".format(self.openports))
        print("Port state: {}").format(self.portstate)
        print("Port protocol: {}".format(self.portservice))
        print("Port OS: {}").format(self.portoperatingsystem)
        print("Operating System: {}").format(self.operatingsystem)
        print("IoT temp F deg: {}").format(self.iottemp)
        print("IoT cpu capacity: {}").format(self.iotcpu)
        print("IoT memory capacity: {}").format(self.iotmem)
	

def sendiotdata(totaldevices,topic):
	iotdevice = 1
	while iotdevice <= totaldevices:
		print("IoT device no."), iotdevice
		iotdeviceinfo = IoTdeviceScanData(randomip(1), openport(), stateport(), serviceport(openport()), portos(serviceport(openport())),os(),iottemp(),iotcpu(),iotmem())
		iotstring = {"IoT temp F deg": "%s" %iotdeviceinfo.iottemp, "IoT cpu capacity": "%s" %iotdeviceinfo.iotcpu, "IoT memory capacity": "%s" %iotdeviceinfo.iotmem, "Operating System": "%s" %iotdeviceinfo.operatingsystem, "Port OS": "%s" %iotdeviceinfo.portoperatingsystem, "Port state": "%s" %iotdeviceinfo.portstate, "Port protocol": "%s" %iotdeviceinfo.portservice, "Open ports": "%s" %iotdeviceinfo.openports, "Initial IP Address": "%s" %iotdeviceinfo.ip_addr}
        	print iotstring
		#producer.send(topic,iotstring)
		time.sleep(3)
		iotdevice += 1
		print('')

# User selectable input for Total IoT devices
totaliotdevices = int(raw_input("Enter total IoT devices: "))
# User selectable input for Kafka topic
topic = str(raw_input("Enter Kafka topic: "))


# Send IoT device info to Kafka broker
sendiotdata(totaliotdevices,topic)
