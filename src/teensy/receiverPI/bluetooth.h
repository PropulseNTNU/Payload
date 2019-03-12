#ifndef BLUETOOTH_H
#define BLUETOOTH_H

#include <SPI.h>
#include <RF24.h>

#define LED_pin 13
#define SCK_PIN 27
#define CE_PIN 6
#define CSN_PIN 7


void initMessage();

void setupBle();

char* retriveMessageBle();

void sendMessage(const char message);

void messageFromPayload();


#endif