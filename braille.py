import board
import touchio

import time

dot1 = touchio.TouchIn(board.A1)
dot2 = touchio.TouchIn(board.A2)
dot3 = touchio.TouchIn(board.A3)
dot4 = touchio.TouchIn(board.A4)
dot5 = touchio.TouchIn(board.A5)
dot6 = touchio.TouchIn(board.A6)
backspace = touchio.TouchIn(board.A7)


# 6 dots plus backspace
dots_to_letter = {
0b1000000: "A",
0b1100000: "B",
0b1001000: "C",
0b1001100: "D",
0b1000100: "E",
0b1101000: "F",
0b1101100: "G",
0b1100100: "H",
0b0101000: "I",
0b0101100: "J",
0b1010000: "K",
0b1110000: "L",
0b1011000: "M",
0b1011100: "N",
0b1010100: "O",
0b1111000: "P",
0b1111100: "Q",
0b1110100: "R",
0b0111000: "S",
0b0111100: "T",
0b1010010: "U",
0b1110010: "V",
0b0101110: "W",
0b1011010: "X",
0b1011110: "Y",
0b1010110: "Z",
0b0000001: "backspace",
}

def readDots():
    dots = int(backspace.value) | int(dot6.value) << 1  | int(dot5.value) << 2 | int(dot4.value) << 3 | int(dot3.value) << 4 | int(dot2.value) << 5 | int(dot1.value) << 6
    return dots

def readKeyboard():
    dots = readDots()
    while dots == 0b0:
        time.sleep(0.1)
        dots = readDots()
        #print("ceros")
    print(bin(dots))
    print(dots_to_letter.keys())
    print(dots_to_letter[dots])
    time.sleep(1)