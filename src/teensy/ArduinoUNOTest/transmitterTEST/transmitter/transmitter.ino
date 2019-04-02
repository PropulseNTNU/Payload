/*
* Arduino Wireless Communication Tutorial
*     Example 1 - Transmitter Code
*                
* by Dejan Nedelkovski, www.HowToMechatronics.com
* 
* Library: TMRh20/RF24, https://github.com/tmrh20/RF24/
*/
#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>
//#define LED_pin 13
#define SCK_PIN 27
#define CE_PIN 6
#define CSN_PIN 7

// ce, csn pins
RF24 radio(CE_PIN, CSN_PIN); 
const byte address[6] = "00001";
void setup() {
  radio.begin();
  SPI.setSCK(SCK_PIN);
  radio.openWritingPipe(address);
  radio.setPALevel(RF24_PA_MIN);
  radio.stopListening();
}
void loop() {
  const char text[] = "Hello World";
  radio.write(&text, sizeof(text));
  delay(1000);
}
