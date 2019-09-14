# Payload

## Run Bluetooth  

### Run on Raspberry PI

Go to: src/rasspberryPI/bluetooth/NRF24L01/

Then run "blePITeensy.py" (in PI terminal: > python blePITeensy.py) 

### Run on Teensy 3.6

Go to: src/teensy/receiverPI/

Add all the libraries in library folder (SPI-master & RF24).

Then run "receiverPI.ino" 


### To start programs automatic from Raspberry PI

> sudo nano .bashrc

and declare filepath (with run command) 



![IMU visualization](/home/marius/Development/Payload/2019-06-17-113045_1824x984_scrot.png)


![Data](/home/marius/Development/Payload/flight_data.png)
