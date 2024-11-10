ADD 10 Key V2

Welcome to ADD 10 Key V2! This is the second version of my custom numpad project, designed to add seamless functionality and dynamic lighting effects to any keyboard setup.
Overview

ADD 10 Key V2 is a minimalistic yet functional numpad powered by CircuitPython and the kmk library. The main features include:

    NumLock-responsive RGB LEDs: The RGB lighting changes based on the NumLock state, creating a visual cue for the numpad's status.
    Sine-wave RGB animation: LEDs smoothly transition through colors when NumLock is enabled, creating a colorful animation.

Full Project Write-Up

For a detailed breakdown of the project, check out the write-up on my blog at pretendgineer.com.
Prerequisites

To use this code, ensure you have the following:

    CircuitPython-compatible microcontroller: This code was designed for RP2040-based boards.
    Keyboard library (KMK): You’ll need to install the kmk library to handle keyboard matrix scanning and HID output.
    PWM support: The board needs to support PWM outputs to control RGB LEDs (common anode).

Installation

    Set up CircuitPython on your board and copy the necessary libraries.
    Install the KMK library in your lib folder.
    Copy this script to your board’s main file (code.py or equivalent).

Usage
RGB Lighting with NumLock

    NumLock on: LEDs transition through RGB colors.
    NumLock off: LEDs turn off, signaling that the numpad is deactivated.

Key Layout

The numpad has a traditional layout, with common keys such as NumLock, Backspace, and Enter. Here’s the layout for reference:

NLCK | / | * | ⌫
-----------------
  7  | 8 | 9 | +
-----------------
  4  | 5 | 6 | 
-----------------
  1  | 2 | 3 | ⏎
-----------------
      0   0   .

Keymap Configuration

This code defines a custom keymap using KMKKeyboard and supports a 4x5 grid with columns configured for your board’s pins.
Support

If you encounter any issues or have questions, feel free to create an issue or contribute directly. You can also reach out on my blog, pretendgineer.com, where I post detailed project guides and updates.
