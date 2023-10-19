import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setwarnings(False)

def flash_led(repeat):
    for i in range(0, repeat):
        GPIO.output(11, True)
        GPIO.output(8, False)
        time.sleep(0.05)
        GPIO.output(11, False)
        GPIO.output(8, True)
        time.sleep(0.05)
    GPIO.cleanup()
    

if __name__ == '__main__':
    flash_led(100)
    