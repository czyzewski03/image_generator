#!/usr/bin/env python

import sys
import os
import random

from PIL import Image

def generate_RGB():
    """Generates random values between 0 and 255 for each RGB channel and returns them in a tuple."""
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    return (red_value, green_value, blue_value)


# Checks that the width and height arguments have been provided and stores them.
if len(sys.argv) < 2:
    print('Usage: py image_generator.py [width] [height]')
    sys.exit()
width = int(sys.argv[1])
height = int(sys.argv[2])

# Creates a new blank image.
image_file = Image.new('RGB', (width, height))
image_pixels = image_file.load()

# Each pixel is changed into a randomly-generated color.
for x in range(width):
    for y in range(height):
        image_pixels[x, y] = generate_RGB()

image_file.save('image.png')