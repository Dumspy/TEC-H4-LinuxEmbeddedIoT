#! /bin/python

import argparse
from sense_hat import SenseHat
import time
import signal
import sys

parser = argparse.ArgumentParser(description="Sense HAT temp/humidity display")
parser.add_argument(
    "-p",
    choices=["temp", "fugt"],
    help="Start mode: temp or fugt",
    default="temp",
    nargs="?",
)
args = parser.parse_args()

sense = SenseHat()

# Display mode: True for temperature, False for humidity
display_temp = True if args.p == "temp" else False
rotation = 0  # Default rotation


# Joystick event handlers
def handle_up(event):
    global rotation
    if event.action != "released":
        rotation = 0
        sense.set_rotation(rotation)


def handle_right(event):
    global rotation
    if event.action != "released":
        rotation = 90
        sense.set_rotation(rotation)


def handle_down(event):
    global rotation
    if event.action != "released":
        rotation = 180
        sense.set_rotation(rotation)


def handle_left(event):
    global rotation
    if event.action != "released":
        rotation = 270
        sense.set_rotation(rotation)


def handle_middle(event):
    global display_temp
    if event.action != "released":
        display_temp = not display_temp


sense.stick.direction_up = handle_up
sense.stick.direction_right = handle_right
sense.stick.direction_down = handle_down
sense.stick.direction_left = handle_left
sense.stick.direction_middle = handle_middle


def draw_mode_dot():
    if display_temp:
        sense.set_pixel(0, 0, 255, 0, 0)  # Red for temperature
    else:
        sense.set_pixel(0, 0, 0, 0, 255)  # Blue for humidity


def cleanup(signum=None, frame=None):
    sense.clear()
    print("Exiting...")
    sys.exit(0)


signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)

try:
    while True:
        if display_temp:
            value = sense.get_temperature()
        else:
            value = sense.get_humidity()
        value_str = f"{value:.1f}"
        for char in value_str:
            sense.show_letter(char, text_colour=[255, 255, 255], back_colour=[0, 0, 0])
            draw_mode_dot()
            time.sleep(0.7)
        sense.clear()
        draw_mode_dot()
        time.sleep(3)
except Exception:
    cleanup()
