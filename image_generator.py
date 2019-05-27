#!/usr/bin/env python

import logging
import random

logging.basicConfig(level=logging.DEBUG,
                    format= '%(asctime)s - %(levelname)s - %(message)s')

def generate_color_hex():
    """Generates random values between 0 and 255 for each colour channel and returns a hex colour code."""
    red_value = random.randint(0, 255)
    green_value = random.randint(0, 255)
    blue_value = random.randint(0, 255)
    return f'#{red_value:02x}{green_value:02x}{blue_value:02x}'

print(generate_color_hex())