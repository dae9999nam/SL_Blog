from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep

def pushed_middle(event):
    print(round(temp,2))


sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
print(pressure)

temp = sense.get_temperature()
print(temp)

humidity = sense.get_humidity()
print(humidity)

sense.stick.direction_middle = pushed_middle
