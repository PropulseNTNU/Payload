#!/usr/bin/env python3
import RPi.GPIO as GPIO
from lib_nrf24 import NRF24
import time
import spidev

global linecounter
numberOfSensors = 16 
stringData = "/home/pi/Payload/src/sensory/Data.txt"

def findNumberOfLines(fileName):
	i = 0
	with open(fileName) as f:
		for i, l in enumerate(f):
			pass
	return i + 2

def bleSetup():
	global linecounter
	linecounter = findNumberOfLines(stringData)
	print("Linecounter: ",linecounter)
	#linecounter = 1
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


def sendMessage(message, conn):
	conn.write(message)
	print("Sent the message: {}".format(message))
	time.sleep(1/100)
	

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
	global linecounter
	if linecounter < 0:
		print("Error in linecount from file")
		
	try: 
		file = open(stringData, 'r')
		print("Linecounter: ",linecounter)
		textfile = file.readlines()[linecounter:]
		
		
	except IOError:
		print("Error in opening file")
	file.close
	
	if textfile == []:
		print("file is empty")												
		return
	element = 0	
	i = 0
	sensorID = 1
	while(element != '\n' and i < len(textfile[0])):
		message = []
		element = textfile[0][i]
		while(element != '\t' and element != '\n' and i < len(textfile[0])):	
			element = textfile[0][i]
						
			if element != '\t' and element != '\n':
				message.append(element)
			i += 1
		
		stringtoint = str(sensorID)
		if sensorID > 9:
			firstDigit = stringtoint[0]
			secondDigit = stringtoint[1]
			message.append(firstDigit)
			message.append(secondDigit)
		
		
		else:
			message.append("-")
			message.append(str(sensorID))
				
		while len(message) < 32:
				message.append(0)
		
		sensorID += 1
		sendMessage(message, conn)
	
	linecounter += 1
	

#def main():
#	conn = bleSetup()

#	message = list("Done")
	
#	while(1):
		#sendSensorData(conn)
		#sendMessage(message, conn)
		#recieveMessage(conn)
				
		#time.sleep(1)
	

#if  __name__ == "__main__":
#	main()
