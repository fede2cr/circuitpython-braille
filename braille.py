import board
import touchio
import time

import alphabet

# For Adafruit's CircuitPlayground Express
dot1 = touchio.TouchIn(board.A1)
dot2 = touchio.TouchIn(board.A2)
dot3 = touchio.TouchIn(board.A3)
dot4 = touchio.TouchIn(board.A4)
dot5 = touchio.TouchIn(board.A5)
dot6 = touchio.TouchIn(board.A6)
backspace = touchio.TouchIn(board.A7)

def dotsToBinary():
    binaryDots = int(backspace.value) | int(dot6.value) << 1  | int(dot5.value) << 2 | int(dot4.value) << 3 | int(dot3.value) << 4 | int(dot2.value) << 5 | int(dot1.value) << 6
    return binaryDots

def readDots():
    dots = dotsToBinary()
    while dots == 0 and dots not in alphabet.dots_to_alphabet.keys():
        dots = dotsToBinary()
        old_dots = dots
        time.sleep(0.1)
        dots = dotsToBinary()
        if old_dots == dots:
            return dots