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
0b1000000: "a", # ⠁
0b1100000: "b", # ⠃
0b1001000: "c", # ⠉
0b1001100: "d", # ⠙
0b1000100: "e", # ⠑
0b1101000: "f", # ⠋
0b1101100: "g", # ⠛
0b1100100: "h", # ⠓
0b0101000: "i", # ⠊
0b0101100: "j", # ⠚
0b1010000: "k", # ⠅
0b1110000: "l", # ⠇
0b1011000: "m", # ⠍
0b1011100: "n", # ⠍
0b1010100: "o", # ⠕
0b1111000: "p", # ⠕
0b1111100: "q", # ⠟
0b1110100: "r", # ⠗
0b0111000: "s", # ⠗
0b0111100: "t", # ⠞
0b1010010: "u", # ⠥
0b1110010: "v", # ⠧
0b0101110: "w", # ⠺
0b1011010: "x", # ⠭
0b1011110: "y", # ⠽
0b1010110: "z", # ⠵
0b0000001: "backspace",
}

# 6 dots plus backspace
dots_to_braille = {
0b1000000: "⠁", # a
0b1100000: "⠃", # b
0b1001000: "⠉", # c
0b1001100: "⠙", # d
0b1000100: "⠑", # e
0b1101000: "⠋", # f
0b1101100: "⠛", # g
0b1100100: "⠓", # h
0b0101000: "⠊", # i
0b0101100: "⠚", # j
0b1010000: "⠅", # k
0b1110000: "⠇", # l
0b1011000: "⠍", # m
0b1011100: "⠍", # n
0b1010100: "⠕", # o
0b1111000: "⠕", # p
0b1111100: "⠟", # q
0b1110100: "⠗", # r
0b0111000: "⠗", # s
0b0111100: "⠞", # t
0b1010010: "⠥", # u
0b1110010: "⠧", # v
0b0101110: "⠺", # w
0b1011010: "⠭", # x
0b1011110: "⠽", # y
0b1010110: "⠵", # z
0b0000001: "backspace",
}


def readDots():
    dots = int(backspace.value) | int(dot6.value) << 1  | int(dot5.value) << 2 | int(dot4.value) << 3 | int(dot3.value) << 4 | int(dot2.value) << 5 | int(dot1.value) << 6
    while dots == 0 and dots not in dots_to_letter.keys():
        dots = int(backspace.value) | int(dot6.value) << 1  | int(dot5.value) << 2 | int(dot4.value) << 3 | int(dot3.value) << 4 | int(dot2.value) << 5 | int(dot1.value) << 6
    return dots