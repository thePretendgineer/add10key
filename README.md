# ADD 10-Key

I very much recommend folks use their own code, I'm an idiot and have no idea what I'm doing.\
That said, this works great. Debounce seems to be fine for my switches, but adjust as needed.

The following writeup is ChatGPT generated.

## Overview

This project aims to create a DIY numpad for those missing one on their compact keyboards, using the RP2040 microcontroller (like the Wisd Tiny RP2040 or a Raspberry Pi Pico). The keypad replicates a typical numpad layout with keys ranging from numeric values (0-9) to function keys like Num Lock, Backspace, Enter, and arithmetic operators (`+`, `/`, `*`). It also supports backspace hold for easy text editing. This guide and code are brought to you by thePretendgineer, where engineering meets hands-on experimentation.

## Components

- **Microcontroller**: Wisd Tiny RP2040 (or equivalent RP2040-based board)
- **Push Button Switches**: 17 buttons for the keypad
- **Breadboard/Wires**: For wiring connections

## GPIO Pin Mapping for Keypad

Below is a complete list of GPIO pins and their assigned keys:

| GPIO Pin | Assigned Key        |
| -------- | ------------------- |
| GP0      | Num Lock            |
| GP1      | `/` (Forward Slash) |
| GP2      | `*` (Asterisk)      |
| GP3      | Backspace           |
| GP4      | Keypad 7            |
| GP5      | Keypad 8            |
| GP6      | Keypad 9            |
| GP7      | Keypad 4            |
| GP8      | Keypad 5            |
| GP9      | Keypad 6            |
| GP10     | Keypad 1            |
| GP11     | Keypad 2            |
| GP12     | Keypad 3            |
| GP13     | Enter               |
| GP14     | Keypad 0            |
| GP15     | `.` (Period)        |
| GP16     | `+` (Plus)          |

## Features

- **Num Lock Key**: Toggle Num Lock functionality to enable or disable the keypad.
- **Backspace Hold**: Allows you to hold down Backspace for continuous deletion, just like on a typical keyboard.
- **Per-Key Debouncing**: Each key is debounced independently to minimize accidental multiple presses.
- **Improved Responsiveness**: Optimized loop delay for better overall responsiveness, ensuring that each key press feels instant.

## Wiring Instructions

- Connect each key switch to the corresponding GPIO pin on the RP2040 board as shown in the GPIO Pin Mapping table.
- Each button should also be connected to **ground** so that when pressed, it pulls the GPIO pin low.
- Internal pull-up resistors are activated via software to simplify wiring, reducing the need for external resistors.

## Installation and Usage

1. **CircuitPython Setup**: Flash CircuitPython onto your RP2040 microcontroller if it's not already installed. You can get it from [CircuitPython.org](https://circuitpython.org/board/raspberry_pi_pico/).
2. **Library Installation**: You need the `adafruit_hid` library to use USB HID functionalities. Download the latest Adafruit CircuitPython Library Bundle from [CircuitPython Libraries](https://circuitpython.org/libraries) and copy the `adafruit_hid` folder to the `lib` directory on your `CIRCUITPY` drive.
3. **Code Upload**: Save the provided `code.py` script in the root of your `CIRCUITPY` drive. The script should run automatically once saved.
4. **Testing**: Connect the RP2040 to your computer. It should be recognized as a USB HID device, and pressing the keys on your DIY keypad should type as expected.

## Code Explanation

The code initializes all 17 keys as digital inputs, each with a pull-up resistor to handle the physical button presses. The Num Lock state is tracked to toggle the keypad's functionality, while the Backspace key is configured to allow holding for continuous operation.

### Key Debouncing

Each key has its own state-tracking mechanism (`last_pressed`) to ensure that each key press registers once until the key is released. This minimizes false triggering and improves reliability.

### Backspace Handling

The code allows for holding the Backspace key without any additional delay, making it practical for real editing use.

## Troubleshooting

- **No Response**: Ensure that `adafruit_hid` is correctly placed in the `lib` folder of the `CIRCUITPY` drive.
- **Multiple Key Presses**: If you experience multiple key registrations per press, try adjusting the loop delay or double-check your wiring.
- **Laggy Response**: The latest version has optimized delay values to improve responsiveness. If it still feels laggy, consider reducing the loop delay further.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). Feel free to modify and share as long as any derivative work is also open-source and distributed under the same license.. Feel free to modify and share as you wish.

## Contributing

Pull requests are welcome. For significant changes, please open an issue first to discuss what you would like to change. Collaboration and feedback are always appreciated!

