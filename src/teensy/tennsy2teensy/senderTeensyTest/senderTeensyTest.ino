#include<SPI.h>
#include<RF24.h>

//#define LED_pin 13
#define SCK_PIN 27
#define CE_PIN 6
#define CSN_PIN 7
 
RF24 conn(CE_PIN, CSN_PIN); 
 
void setup(void){
  while(!Serial);
  Serial.begin(9600);
  SPI.setSCK(SCK_PIN);
  conn.begin();
  conn.setPALevel(RF24_PA_MAX);
  conn.setChannel(0x76);
  conn.openWritingPipe(0xF0F0F0F0E1LL);
  const uint64_t pipe = (0xE8E8F0F0E1LL);
  conn.openReadingPipe(1, pipe);
 
  conn.enableDynamicPayloads();
  conn.powerUp();
  
}
 
void loop(void){
  conn.startListening();
  Serial.println("Starting loop. bluetooth on.");
  char receivedMessage[32] = {0};
  if(conn.available()){
    conn.read(receivedMessage, sizeof(receivedMessage));
    Serial.println(receivedMessage);
    Serial.println("Turning off the conn.");
    conn.stopListening();
 
    String stringMessage(receivedMessage);
 
    /*if(stringMessage == "GETSTRING"){
      Serial.println("Looks like they want a string!");
      const char text[] = "Yo wassup, haha";
      conn.write(text, sizeof(text));
      Serial.println("We sent our message.");
    }*/
  }
  delay(1000);
 
}
