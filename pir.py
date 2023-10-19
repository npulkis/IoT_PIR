import RPi.GPIO as GPIO
import time

PIR_pin = 16
Buzzer_pin = 8

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIR_pin, GPIO.IN)
GPIO.setup(Buzzer_pin, GPIO.OUT)

def main():
    motion_detected()
def buzz(repeat):
    for i in range(0, repeat):
        for pulse in range(60):
            GPIO.output(Buzzer_pin, True)
            time.sleep(0.001)
            GPIO.output(Buzzer_pin, False)
            time.sleep(0.001)
        time.sleep(0.05)

def motion_detected():
    while(True):
        if GPIO.input(PIR_pin):
            print("Motion Detected...")
            buzz(4)
            time.sleep(2)
        else:
            print("No Motion Detected...")
            time.sleep(2)

if __name__ == 'main':
    main()
