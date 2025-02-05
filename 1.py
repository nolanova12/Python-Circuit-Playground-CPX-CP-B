import time
import board
import neopixel
from adafruit_circuitplayground import cp

# Set up NeoPixels on Circuit Playground Express
pixels = cp.pixels
pixels.brightness = 0.3  # Adjust brightness (0.0 to 1.0)

# List of colors for the nightlight
colors = [
    (255, 0, 0),   # Red
    (0, 255, 0),   # Green
    (0, 0, 255),   # Blue
    (255, 255, 0), # Yellow
    (0, 255, 255), # Cyan
    (255, 0, 255)  # Magenta
]
'''
while True:
    for color in colors:
        pixels.fill(color)  # Change all pixels to current color
        time.sleep(1)  # Delay before switching to the next color
'''

while True:
    if cp.shake():  # Detect motion
        for color in colors:
            pixels.fill(color)
            time.sleep(1)
    else:
        pixels.fill((0, 0, 0))  # Turn off when no motion detected

