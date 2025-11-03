from sense_hat import SenseHat
import time

sense = SenseHat()

# Turn on a single LED (top-left corner, red)
sense.set_pixel(0, 0, 255, 0, 0)

try:
    while True:
        temp = sense.get_temperature()
        humidity = sense.get_humidity()
        print(f"Temperature: {temp:.2f} C, Humidity: {humidity:.2f} %")
        time.sleep(5)
except KeyboardInterrupt:
    sense.clear()  # Turn off LEDs on exit
    print("Exiting...")
