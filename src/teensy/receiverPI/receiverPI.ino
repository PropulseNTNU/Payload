//SendReceive.ino

#include "bluetooth.h"

void setup(void){
  setupBle();
  pinMode(LED_pin, OUTPUT);
  digitalWrite(LED_pin, HIGH);
  delay(200);
  digitalWrite(LED_pin, LOW); 
}

void loop(void){
  messageFromPayload();
  
}

