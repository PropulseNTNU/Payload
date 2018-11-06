import RPi.GPIO as GPIO
import time


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT) #Use pin 7


def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return


def main():
    setup()

    while True:
        blink(7)

    # GPIO.cleanup()


main()
