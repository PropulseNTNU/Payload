import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

def bleSetup():
	GPIO.setmode(GPIO.BCM)

	pipes = [[0xE8, 0xE8, 0xF0, 0xF0, 0xE1], [0xF0, 0xF0, 0xF0, 0xF0, 0xE1]]

	conn = NRF24(GPIO, spidev.SpiDev())
	conn.begin(0, 17)

	conn.setPayloadSize(32)
	conn.setChannel(0x76) #endre paa kanal for aa legge til flere bleenheter
	conn.setDataRate(NRF24.BR_1MBPS)
	conn.setPALevel(NRF24.PA_MIN)

	conn.setAutoAck(True)
	conn.enableDynamicPayloads()
	conn.enableAckPayload()

	conn.openWritingPipe(pipes[0])
	conn.openReadingPipe(1, pipes[1])
	conn.printDetails()
	# conn.startListening()
	return conn


def sendMessage(message, radio):
	radio.write(message)
	print("Sent the message: {}".format(message))
	time.sleep(1)
	

def recieveMessage(conn):
	start = time.time()
	conn.startListening()
	
	while not conn.available(0):
	   time.sleep(1 / 100)
	   if time.time() - start > 2:
	       print("Timed out.")
	       break
	
	receivedMessage = []
	conn.read(receivedMessage, conn.getDynamicPayloadSize())
	print("Received: {}".format(receivedMessage))
	
	print("Translating the receivedMessage into unicode characters")
	string = ""
	for n in receivedMessage:
		# Decode into standard unicode set
	    if (n >= 32 and n <= 126):
	        string += chr(n)
	print("Out received message decodes to: {}".format(string))
	conn.stopListening()
	

def sendSensorData(conn):
	file = open("testSensorData.txt", 'r')
	textfile = file.readlines()[1:]
	file.close
	for row in textfile: 	
		for element in row.split():
			message = []
			message.append(element)
			#while len(message) < 32:
			#	message.append(0)
			#print(message)
			sendMessage(element, conn)
	
	

def main():
	conn = bleSetup()

	message = list("Done")
	
	while(1):
		sendSensorData(conn)
		sendMessage(message, conn)
		#recieveMessage(conn)
				
		time.sleep(1)
	
main()

