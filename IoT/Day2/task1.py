from sense_hat import SenseHat, ACTION_PRESSED
from time import sleep
import time, datetime
import os



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


f = open("record.txt", "w")
# for i in range(50):
n = 0
while n < 50:
    datenow = datetime.datetime.now()
    r_temp = round(temp, 2)
    f.write(f"{datenow}\t{r_temp}\n")
    n += 1
    sleep(1)
f.close()