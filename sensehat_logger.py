from sense_hat import SenseHat
import time

sense = SenseHat()

# Initial dot position
x, y = 0, 0
DOT_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)


# Clamp function to keep dot within bounds
def clamp(val, min_val=0, max_val=7):
    return max(min_val, min(max_val, val))


def draw_dot():
    sense.clear(BG_COLOR)
    sense.set_pixel(x, y, *DOT_COLOR)


def move_up(event):
    global y
    if event.action != "released":
        y = clamp(y - 1)
        draw_dot()


def move_down(event):
    global y
    if event.action != "released":
        y = clamp(y + 1)
        draw_dot()


def move_left(event):
    global x
    if event.action != "released":
        x = clamp(x - 1)
        draw_dot()


def move_right(event):
    global x
    if event.action != "released":
        x = clamp(x + 1)
        draw_dot()


sense.stick.direction_up = move_up
sense.stick.direction_down = move_down
sense.stick.direction_left = move_left
sense.stick.direction_right = move_right

draw_dot()

try:
    while True:
        temp = sense.get_temperature()
        humidity = sense.get_humidity()
        print(f"Temperature: {temp:.2f} C, Humidity: {humidity:.2f} %")
        time.sleep(5)
except KeyboardInterrupt:
    sense.clear()  # Turn off LEDs on exit
    print("Exiting...")
