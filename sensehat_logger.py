#! /bin/python

from sense_hat import SenseHat
import time

sense = SenseHat()

# Display mode: True for temperature, False for humidity
display_temp = True
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

try:
    while True:
        if display_temp:
            value = sense.get_temperature()
        else:
            value = sense.get_humidity()
        value_str = f"{value:.1f}"
        for char in value_str:
            sense.show_letter(char, text_colour=[255, 255, 255], back_colour=[0, 0, 0])
            time.sleep(0.7)
        time.sleep(3)
except KeyboardInterrupt:
    sense.clear()
    print("Exiting...")
