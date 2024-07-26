import RPi.GPIO as GPIO
import time
import _thread

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

redLED = 4
GPIO.setup(redLED, GPIO.OUT)

greenLED = 8
GPIO.setup(greenLED, GPIO.OUT)

waitLED = 7
GPIO.setup(waitLED, GPIO.OUT)

button = 15
GPIO.setup(button, GPIO.IN, GPIO.PUD_UP)

global button_pressed
button_pressed = False

global red_5
red_5 = False

global x
x = False

def button_reader_thread():
    global button_pressed
    while True:
        if GPIO.input(button) == False:
            start_time = time.time()
            while (GPIO.input(button) == False):
                pass
            end_time = time.time()
            interval = end_time - start_time
            if interval > 0.5:
                button_pressed = True

def red_time_check():
    global red_5
    global x
    while True:
        if x == True:
            start_time = time.time()
            while x == True:
                pass
                if time.time() - start_time > 5:
                    a = time.time() - start_time > 5
                    break
            a = 0
            red_5 = True    

_thread.start_new_thread(button_reader_thread, ())
_thread.start_new_thread(red_time_check, ())


cond = 1
while True:
    if cond == 0 and button_pressed == True:
        while True:
            GPIO.output(waitLED, 1)
            if red_5 == True:
                time.sleep(3)
            cond = 1
            red_5 = False
            x = False
            button_pressed = False
            GPIO.output(waitLED, 0)
            break

    if (cond == 1):
        GPIO.output(greenLED, 1)
        GPIO.output(redLED, 0)
        GPIO.output(waitLED, 0)
        time.sleep(5)
        for i in range(3):
            GPIO.output(greenLED, 0)
            time.sleep(0.5)
            GPIO.output(greenLED, 1)
            time.sleep(0.5)
        GPIO.output(greenLED, 0)
        GPIO.output(redLED, 1)
        x = True
        cond = 0


