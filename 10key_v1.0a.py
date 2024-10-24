# Required Libraries
import board
import digitalio
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import time
import math

# Setup Keyboard HID
kbd = Keyboard(usb_hid.devices)

# Pins for the keys
key_pins = [
    board.GP0, board.GP1, board.GP2, board.GP3,  # 1st row (Numlock, '/', '*', 'Delete')
    board.GP4, board.GP5, board.GP6,  # 2nd row ('7', '8', '9')
    board.GP7, board.GP8, board.GP9,  # 3rd row ('4', '5', '6')
    board.GP10, board.GP11, board.GP12,  # 4th row ('1', '2', '3')
    board.GP13, board.GP14, board.GP15,  # 5th row ('Enter', '0', '.')
    board.GP16  # ('+')
]

# Set up the keys as digital inputs with pull-up resistors
keys = []
for pin in key_pins:
    key = digitalio.DigitalInOut(pin)
    key.direction = digitalio.Direction.INPUT
    key.pull = digitalio.Pull.UP
    keys.append(key)

# Defining RGB LED pin and numlock flag
NUMLOCK_LED_PIN = board.GP17
NUMLOCK_LED_NUM = 1
rgb_led = neopixel.NeoPixel(NUMLOCK_LED_PIN, NUMLOCK_LED_NUM, brightness=0.2, auto_write=False)
numlock_enabled = False
rainbow_index = 0

# Helper function to generate colors for the rainbow effect
def colorwheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 85:
        return (int(pos * 3), int(255 - pos * 3), 0)
    elif pos < 170:
        pos -= 85
        return (int(255 - pos * 3), 0, int(pos * 3))
    else:
        pos -= 170
        return (0, int(pos * 3), int(255 - pos * 3))

# Key mapping
key_mapping = [
    Keycode.NUM_LOCK, Keycode.SLASH, Keycode.ASTERISK, Keycode.DELETE,  # Numlock, '/', '*', 'Delete'
    Keycode.KEYPAD_SEVEN, Keycode.KEYPAD_EIGHT, Keycode.KEYPAD_NINE,  # '7', '8', '9'
    Keycode.KEYPAD_FOUR, Keycode.KEYPAD_FIVE, Keycode.KEYPAD_SIX,  # '4', '5', '6'
    Keycode.KEYPAD_ONE, Keycode.KEYPAD_TWO, Keycode.KEYPAD_THREE,  # '1', '2', '3'
    Keycode.ENTER, Keycode.KEYPAD_ZERO, Keycode.KEYPAD_PERIOD, Keycode.KEYPAD_PLUS  # 'Enter', '0', '.', '+'
]

# Main loop
while True:
    # Handle the RGB LED rainbow cycle if Numlock is enabled
    if numlock_enabled:
        rgb_led[0] = colorwheel(rainbow_index & 255)
        rgb_led.show()
        rainbow_index = (rainbow_index + 1) % 256
    else:
        rgb_led.fill((0, 0, 0))  # Turn off LED when numlock is disabled
        rgb_led.show()

    for i, key in enumerate(keys):
        if not key.value:  # When key is pressed
            if key_mapping[i] == Keycode.NUM_LOCK:
                numlock_enabled = not numlock_enabled
                time.sleep(0.2)  # Debounce delay
            elif numlock_enabled:  # Only allow key presses if numlock is enabled
                kbd.press(key_mapping[i])
                time.sleep(0.1)  # Small delay to simulate key press
                kbd.release_all()

    time.sleep(0.01)  # Loop delay to avoid high CPU usage
