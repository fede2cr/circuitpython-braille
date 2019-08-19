import time
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import alphabet

keyboard = Keyboard()
keyboard_layout = KeyboardLayoutUS(keyboard)

def dotsToBinary():
    binaryDots = int(cpx.touch_A7) | int(cpx.touch_A6) << 1  | int(cpx.touch_A5) << 2 | int(cpx.touch_A4) << 3 | int(cpx.touch_A3) << 4 | int(cpx.touch_A2) << 5 | int(cpx.touch_A1) << 6
#    print(bin(binaryDots))
    time.sleep(0.1)
    return binaryDots

def readDots():
    while True:
        dots = dotsToBinary()
        if (dots != 0) or (dots not in alphabet.dots_to_alphabet.keys() ):
            returnDots = dots
            time.sleep(0.01)
        dots = dotsToBinary()
        if dots == returnDots:
            while dotsToBinary() != 0:
                time.sleep(0.01)
            return dots


def keyboardLoop():
    while True:
        dots = readDots()
        if dots in alphabet.dots_to_alphabet.keys():
            if cpx.switch is True:
                print(alphabet.dots_to_alphabet[dots]['latin'])
                print(alphabet.dots_to_alphabet[dots]['braille'])
            else:
                keyboard_layout.write(alphabet.dots_to_alphabet[dots]['latin'])
        time.sleep(0.01)


keyboardLoop()
#braille.gameLoop() # TODO, for learning using a simple game