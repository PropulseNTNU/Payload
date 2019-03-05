//SendReceive.ino

#include<SPI.h>
#include<RF24.h>
#include<string.h>

// CE, CSN pins
RF24 conn(6, 7);
_SPI.setSCK(27); 
const int numberOfSensors = 4;
String fullMessage[numberOfSensors]; //message sent to the telemetry

void initMessage(){
  for(int i = 0; i < numberOfSensors; i++){
    fullMessage[i] = "0";
  }  
}

void setupBle(void){
  while(!Serial);
  Serial.begin(9600);
  
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

char* retriveMessageBle(void){
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

void messageFromPayload(){
  String message =  String(retriveMessageBle());
  int index = 0;
  index = message.length();
  if(index > 0){
    uint8_t messageID = uint8_t(message[index - 1]) - 48; //ASCII fixing 
    fullMessage[messageID] = String(message);//[int(messageID)] = String(message);
    Serial.println(fullMessage[messageID]);
      
  }
  Serial.println("No reading");    
  delay(200);
}

void setup(void){
  setupBle();
}

void loop(void){
  messageFromPayload();
  
}

