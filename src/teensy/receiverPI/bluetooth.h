#ifndef BLUETOOTH_H
#define BLUETOOTH_H

#include <SPI.h>
#include <RF24.h>

#define LED_pin 13
#define SCK_PIN 27
#define CE_PIN 6
#define CSN_PIN 7


void initMessage(double* data, int NUM_SENSORS);

void setupBle(double* data, int NUM_SENSORS);

char* retriveMessageBle();

void sendMessage(const char message);

/* Updates the sensor array with values from bluetooth. */

int messageFromPayload(double* data);

#endif
