//Send.ino
 
#include<SPI.h>
#include<RF24.h>

//#define LED_pin 13
#define SCK_PIN 27
#define CE_PIN 6
#define CSN_PIN 7

// ce, csn pins
RF24 conn(CE_PIN, CSN_PIN); 
 
void setup(void){
  conn.begin();
  SPI.setSCK(SCK_PIN);
  conn.setPALevel(RF24_PA_MAX);
  conn.setChannel(0x76);
  conn.openWritingPipe(0xF0F0F0F0E1LL);
  conn.enableDynamicPayloads();
  conn.powerUp();
 
}
 
void loop(void){
  const char text[] = "Hello World is awesome";
  conn.write(&text, sizeof(text));
  Serial.println("Sending!");
  delay(1000);
 
}
