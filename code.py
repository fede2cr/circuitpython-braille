import time
import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import alphabet

dot1 = digitalio.DigitalInOut(board.D3)
dot1.direction = digitalio.Direction.INPUT
dot1.pull = digitalio.Pull.UP
dot2 = digitalio.DigitalInOut(board.D4)
dot2.direction = digitalio.Direction.INPUT
dot2.pull = digitalio.Pull.UP
dot3 = digitalio.DigitalInOut(board.D7)
dot3.direction = digitalio.Direction.INPUT
dot3.pull = digitalio.Pull.UP
dot4 = digitalio.DigitalInOut(board.D12)
dot4.direction = digitalio.Direction.INPUT
dot4.pull = digitalio.Pull.UP
dot5 = digitalio.DigitalInOut(board.D11)
dot5.direction = digitalio.Direction.INPUT
dot5.pull = digitalio.Pull.UP
dot6 = digitalio.DigitalInOut(board.D10)
dot6.direction = digitalio.Direction.INPUT
dot6.pull = digitalio.Pull.UP
space = digitalio.DigitalInOut(board.A2)
space.direction = digitalio.Direction.INPUT
space.pull = digitalio.Pull.UP
enter = digitalio.DigitalInOut(board.D2)
enter.direction = digitalio.Direction.INPUT
enter.pull = digitalio.Pull.UP
backspace = digitalio.DigitalInOut(board.D9)
backspace.direction = digitalio.Direction.INPUT
backspace.pull = digitalio.Pull.UP

keyboard = Keyboard()
keyboard_layout = KeyboardLayoutUS(keyboard)

def dotsToBinary():
#    binaryDots = 0 | int(not enter.value) << 1 | int(not space.value) << 2 | int(not dot6.value) << 3  | int(not dot5.value) << 4 | int(not dot4.value) << 5 | int(not dot3.value) << 6 | int(not dot2.value) << 7 | int(not dot1.value) << 8
    binaryDots = int(not enter.value) | int(not space.value) << 1 | int(not backspace.value) << 2 | int(not dot6.value) << 3  | int(not dot5.value) << 4 | int(not dot4.value) << 5 | int(not dot3.value) << 6 | int(not dot2.value) << 7 | int(not dot1.value) << 8

# For Playground
#    binaryDots = int(cpx.button_b) | int(cpx.button_a) << 1 | int(cpx.touch_A7) << 2 | int(cpx.touch_A6) << 3  | int(cpx.touch_A5) << 4 | int(cpx.touch_A4) << 5 | int(cpx.touch_A3) << 6 | int(cpx.touch_A2) << 7 | int(cpx.touch_A1) << 8
    print(bin(binaryDots))
    time.sleep(0.1)
    return binaryDots

def readDots():
    while True:
        dots = dotsToBinary()
        if (dots != 0) or (dots not in alphabet.dots_to_alphabet.keys() ):
            returnDots = dots
            time.sleep(0.01)
        dots = dotsToBinary()
        if (dots != 0 ) and (dots == returnDots) and (dots in alphabet.dots_to_alphabet.keys() ):
#            cpx.play_tone(440, 0.1)
            while dotsToBinary() != 0:
                time.sleep(0.01)
            return dots


def keyboardLoop():
    while True:
        dots = readDots()
        print(alphabet.dots_to_alphabet[dots]['latin'])
        print(alphabet.dots_to_alphabet[dots]['braille'])
        if 'keycode' in alphabet.dots_to_alphabet[dots]:
            keyboard.press(alphabet.dots_to_alphabet[dots]['keycode'])
            keyboard.release_all()
        else:
            keyboard_layout.write(alphabet.dots_to_alphabet[dots]['latin'])


keyboardLoop()
#braille.gameLoop() # TODO, for learning using a simple game