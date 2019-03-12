

#include "bluetooth.h"

RF24 conn(CE_PIN, CSN_PIN); 
const int numberOfSensors = 10;
String fullMessage[numberOfSensors]; //message sent to the telemetry


void initMessage(){
  for(int i = 0; i < numberOfSensors; i++){
    fullMessage[i] = "0";
  }  
}


void setupBle(){
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
  initMessage();
  Serial.println("Bluetooth setup done");
}


char* retriveMessageBle(){
  conn.startListening();
  char receivedMessage[32] = {0};
  char * buf = (char *) malloc (sizeof(receivedMessage));
  if(conn.available()){
    conn.read(receivedMessage, sizeof(receivedMessage));
    strcpy (buf, receivedMessage);
    conn.stopListening();
    return buf;     
  }
  delay(200);
  //free(receivedMessage);
  return 0;
}


void sendMessage(const char message){
  Serial.println("sending");
  Serial.println(message);
  char text[] = "test1";
  conn.write(&text, sizeof(text));
  delay(1000);
}


//NEEDS MODIFYING
void messageFromPayload(){
  String message =  String(retriveMessageBle());
  int index = 0;
  index = message.length();
  String data; 
  digitalWrite(LED_pin, LOW);
  if(index > 0){
    uint8_t messageIDFirstDigit = uint8_t(message[index-2]) - 48; //ASCII fixing
    uint8_t messageIDSecondDigit = uint8_t(message[index-1]) - 48; //ASCII fixing
   
    Serial.println("ID: ");
    Serial.println(messageIDFirstDigit);
    Serial.println(messageIDSecondDigit);
    Serial.println("Message: ");
    Serial.println(message);
    //fullMessage[messageID] = String(message);
    //Serial.println(fullMessage[10]); 
    digitalWrite(LED_pin, HIGH);
    delay(200);
         
  }
  Serial.println("No reading");    
  delay(200);
}


