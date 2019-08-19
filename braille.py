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
dots_to_alphabet = {
0b1000000: { 'latin': "a", 'braille': '⠁'},
0b1100000: { 'latin': "b", 'braille': '⠃'},
0b1001000: { 'latin': "c", 'braille': '⠉'},
0b1001100: { 'latin': "d", 'braille': '⠙'},
0b1000100: { 'latin': "e", 'braille': '⠑'},
0b1101000: { 'latin': "f", 'braille': '⠋'},
0b1101100: { 'latin': "g", 'braille': '⠛'},
0b1100100: { 'latin': "h", 'braille': '⠓'},
0b0101000: { 'latin': "i", 'braille': '⠊'},
0b0101100: { 'latin': "j", 'braille': '⠚'},
0b1010000: { 'latin': "k", 'braille': '⠅'},
0b1110000: { 'latin': "l", 'braille': '⠇'},
0b1011000: { 'latin': "m", 'braille': '⠍'},
0b1011100: { 'latin': "n", 'braille': '⠍'},
0b1010100: { 'latin': "o", 'braille': '⠕'},
0b1111000: { 'latin': "p", 'braille': '⠕'},
0b1111100: { 'latin': "q", 'braille': '⠟'},
0b1110100: { 'latin': "r", 'braille': '⠗'},
0b0111000: { 'latin': "s", 'braille': '⠗'},
0b0111100: { 'latin': "t", 'braille': '⠞'},
0b1010010: { 'latin': "u", 'braille': '⠥'},
0b1110010: { 'latin': "v", 'braille': '⠧'},
0b0101110: { 'latin': "w", 'braille': '⠺'},
0b1011010: { 'latin': "x", 'braille': '⠭'},
0b1011110: { 'latin': "y", 'braille': '⠽'},
0b1010110: { 'latin': "z", 'braille': '⠵'},
# Simples
0b0010000: { 'latin': "'", 'braille': '⠄'},
0b0110000: { 'latin': ";", 'braille': '⠆'},
0b0100100: { 'latin': ":", 'braille': '⠒'},
# Special and indicators
0b0000010: { 'latin': 'capital', 'braille': '⠠'},
0b0011110: { 'latin': 'number', 'braille': '⠼'},
0b0000001: { 'latin': "backspace", 'braille': ''},
}

def readDots():
    dots = int(backspace.value) | int(dot6.value) << 1  | int(dot5.value) << 2 | int(dot4.value) << 3 | int(dot3.value) << 4 | int(dot2.value) << 5 | int(dot1.value) << 6
    while dots == 0 and dots not in dots_to_alphabet.keys():
        dots = int(backspace.value) | int(dot6.value) << 1  | int(dot5.value) << 2 | int(dot4.value) << 3 | int(dot3.value) << 4 | int(dot2.value) << 5 | int(dot1.value) << 6
    return dots