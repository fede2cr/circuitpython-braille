import braille
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_circuitplayground.express import cpx

keyboard = Keyboard()
keyboard_layout = KeyboardLayoutUS(keyboard)

while True:
    dots = braille.readDots()
    if dots in braille.dots_to_alphabet.keys():
        if cpx.switch is True:
            print(braille.dots_to_alphabet[dots]['latin'])
            print(braille.dots_to_alphabet[dots]['braille'])
        else:
            keyboard_layout.write(braille.dots_to_alphabet[dots]['latin'])
    time.sleep(0.01)