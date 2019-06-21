from microbit import *
import neopixel

# Please tag us if used!
# We'd love to see what you make:
# @ScienceOxford

lights = neopixel.NeoPixel(pin16, 8)

red = (50, 0, 0)
orange = (50, 25, 0)
yellow = (40, 50, 0)
green = (0, 50, 0)
blue = (0, 0, 50)
indigo = (50, 0, 25)
violet = (50, 0, 50)
white = (50, 50, 50)

colours = [red, orange, yellow, green, blue, indigo, violet, white]

for pixel in range(0, 8):
    lights[pixel] = colours[pixel]
lights.show()
