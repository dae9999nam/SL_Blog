from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)
violet = (148, 0, 211)
indigo = (75, 0, 130)
green = (0, 255, 0)
orange = (255, 127, 0)
red = (255, 0, 0)
white = (255, 255, 255)

color_list = [blue, yellow, violet, indigo, green, orange, red, white]

ball_position = [3, 3] # coordinates of the starting position
white = (255, 255, 255)
sense.set_pixel(ball_position[0], ball_position[1], white)

while True:
  rand_idx1 = random.randrange(len(color_list))
  random_color1 = color_list[rand_idx1]
  
  sleep(1)	# sleep for 1 second
  ball_position[0] = random.randint(0, 7) # generate a new x-position
  ball_position[1] = random.randint(0, 7) # generate a new y-position
  sense.clear()
  sense.set_pixel(ball_position[0], ball_position[1], random_color1)