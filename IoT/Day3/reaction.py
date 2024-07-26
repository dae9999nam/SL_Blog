import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 4
GPIO.setup(led, GPIO.OUT)

t = random.uniform(1,3)

GPIO.output(led, 0)
time.sleep(3)
GPIO.output(led, 1)

left_button = 14
right_button = 15

Player1 = input("Please enter the left player name: ")
Player2 = input("Please enter the right player name: ")

GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(right_button, GPIO.IN, GPIO.PUD_UP)



try:
    while True:
        if(GPIO.input(left_button)) == False:
            print(f'{Player1} wins!')
            break
        if(GPIO.input(right_button)) == False:
            print(f'{Player2} wins!')
            break

except keyboardInterrupt:
    print("CTRL-C: Terminating program...")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
