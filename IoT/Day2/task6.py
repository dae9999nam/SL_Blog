from sense_hat import SenseHat
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

while True:
  rand_idx1 = random.randrange(len(color_list))
  rand_idx2 = random.randrange(len(color_list))

  random_color1 = color_list[rand_idx1]
  random_color2 = color_list[rand_idx2]

  sense.show_message("EEE is awesome!", text_colour=random_color1, back_colour=random_color2, scroll_speed=0.05)