import board
import math
import time
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules import Module
from pwmio import PWMOut

class RGBNumLock(Module):
    def __init__(self):
        # Set up PWM for RGB LEDs, initially off
        self.red_led = PWMOut(board.GP12, frequency=5000, duty_cycle=65535)   # Common anode (off)
        self.green_led = PWMOut(board.GP10, frequency=5000, duty_cycle=65535) # Common anode (off)
        self.blue_led = PWMOut(board.GP11, frequency=5000, duty_cycle=65535)  # Common anode (off)
        self.animation_speed = 0.05  # Speed at which colors change
        self.angle = 0
        self.is_numlock_on = False
        self.last_update_time = time.monotonic()

    def after_hid_send(self, keyboard):
        current_numlock = bool(keyboard.led_status.num_lock)

        # Detect NumLock state change
        if current_numlock != self.is_numlock_on:
            self.is_numlock_on = current_numlock
            if not self.is_numlock_on:
                # Turn off all LEDs if NumLock is turned off
                self.red_led.duty_cycle = 65535
                self.green_led.duty_cycle = 65535
                self.blue_led.duty_cycle = 65535
            else:
                # Reset angle to start the cycle smoothly when turning NumLock back on
                self.angle = 0

        # Update LED colors if NumLock is on
        if self.is_numlock_on:
            current_time = time.monotonic()
            if current_time - self.last_update_time >= self.animation_speed:
                self.update_led_colors()
                self.last_update_time = current_time

    def update_led_colors(self):
        # Calculate RGB values based on the sine wave function
        red = int((math.sin(self.angle) * 0.5 + 0.5) * 65535)
        green = int((math.sin(self.angle + 2 * math.pi / 3) * 0.5 + 0.5) * 65535)
        blue = int((math.sin(self.angle + 4 * math.pi / 3) * 0.5 + 0.5) * 65535)

        # Since it's common anode, invert the duty cycle values
        self.red_led.duty_cycle = 65535 - red
        self.green_led.duty_cycle = 65535 - green
        self.blue_led.duty_cycle = 65535 - blue

        # Increment the angle for the animation, wrap around after a full cycle
        self.angle += 0.05
        if self.angle >= 2 * math.pi:
            self.angle -= 2 * math.pi

# Keyboard setup
keyboard = KMKKeyboard()

# Basic keyboard setup
keyboard.col_pins = (board.GP4, board.GP1, board.GP2, board.GP3)
keyboard.row_pins = (board.GP28, board.GP27, board.GP26, board.GP15, board.GP14)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Basic debounce
keyboard.tap_time = 150

# Add RGB module
keyboard.modules.append(RGBNumLock())

# Keymap
keyboard.keymap = [
    [  # Layer 0
        # Row 1
        KC.NLCK, KC.PSLS, KC.PAST, KC.BSPC,
        # Row 2
        KC.P7, KC.P8, KC.P9, KC.PPLS,
        # Row 3
        KC.P4, KC.P5, KC.P6,
        # Row 4
        KC.P1, KC.P1, KC.P2, KC.P3, KC.ENT,
        # Row 5
        KC.P0, KC.P0, KC.PDOT
    ]
]

if __name__ == '__main__':
    keyboard.go()
