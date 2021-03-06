//SendReceive.ino

#include "bluetooth.h"

const int NUM_SENSORS = NUMBER_OF_SENSORS - 1;
double payloadData[NUM_SENSORS]; //message sent to the telemetry


void setup(void){
  while(!Serial);
  Serial.begin(9600);
  setupBle(payloadData, NUM_SENSORS);
  
  Serial.println("Bluetooth setup done");

  //Check if programmed
  pinMode(LED_pin, OUTPUT);
  digitalWrite(LED_pin, HIGH);
  delay(200);
  digitalWrite(LED_pin, LOW); 
}

void loop(void){
  updateDataFromBle(payloadData);
   
  //for testing
  Serial.println("Data");
  for(int i= 0; i < 13; i++){
    Serial.println(payloadData[i]);
  }
}

