import board
import touchio

dot1 = touchio.TouchIn(board.A1)
dot2 = touchio.TouchIn(board.A2)
dot3 = touchio.TouchIn(board.A3)
dot4 = touchio.TouchIn(board.A4)
dot5 = touchio.TouchIn(board.A5)
dot6 = touchio.TouchIn(board.A6)
backspace = touchio.TouchIn(board.A7)


def readKeyboard():
    if dot1.value and not dot2.value and not dot3.value and not dot4.value and not dot5.value and not dot6.value:
        print("A")
    if dot1.value and dot2.value and not dot3.value and not dot4.value and not dot5.value and not dot6.value:
        print("B")
    if dot1.value and not dot2.value and not dot3.value and dot4.value and not dot5.value and not dot6.value:
        print("C")
    if dot1.value and not dot2.value and not dot3.value and dot4.value and dot5.value and not dot6.value:
        print("D")
    if dot1.value and not dot2.value and not dot3.value and not dot4.value and dot5.value and not dot6.value:
        print("E")
    if dot1.value and dot2.value and not dot3.value and dot4.value and not dot5.value and not dot6.value:
        print("F")
    if dot1.value and dot2.value and not dot3.value and dot4.value and dot5.value and not dot6.value:
        print("G")
    if dot1.value and dot2.value and not dot3.value and not dot4.value and dot5.value and not dot6.value:
        print("H")
    if not dot1.value and dot2.value and not dot3.value and dot4.value and not dot5.value and not dot6.value:
        print("I")
    if not dot1.value and dot2.value and not dot3.value and dot4.value and dot5.value and not dot6.value:
        print("J")
    if dot1.value and not dot2.value and dot3.value and not dot4.value and not dot5.value and not dot6.value:
        print("K")
    if dot1.value and dot2.value and dot3.value and not dot4.value and not dot5.value and not dot6.value:
        print("L")
    if dot1.value and not dot2.value and dot3.value and dot4.value and not dot5.value and not dot6.value:
        print("M")
    if dot1.value and not dot2.value and dot3.value and dot4.value and dot5.value and not dot6.value:
        print("N")
    if dot1.value and not dot2.value and dot3.value and not dot4.value and dot5.value and not dot6.value:
        print("O")
    if dot1.value and dot2.value and dot3.value and dot4.value and not dot5.value and not dot6.value:
        print("P")
    if dot1.value and dot2.value and dot3.value and dot4.value and dot5.value and not dot6.value:
        print("Q")
    if dot1.value and dot2.value and dot3.value and not dot4.value and dot5.value and not dot6.value:
        print("R")
    if not dot1.value and dot2.value and dot3.value and dot4.value and not dot5.value and not dot6.value:
        print("S")
    if not dot1.value and dot2.value and dot3.value and dot4.value and dot5.value and not dot6.value:
        print("T")
    if dot1.value and not dot2.value and dot3.value and not dot4.value and not dot5.value and dot6.value:
        print("U")
    if dot1.value and dot2.value and dot3.value and not dot4.value and not dot5.value and dot6.value:
        print("V")
    if not dot1.value and dot2.value and not dot3.value and dot4.value and dot5.value and dot6.value:
        print("W")
    if dot1.value and not dot2.value and dot3.value and dot4.value and not dot5.value and dot6.value:
        print("X")
    if dot1.value and not dot2.value and dot3.value and dot4.value and dot5.value and dot6.value:
        print("Y")
    if dot1.value and not dot2.value and dot3.value and not dot4.value and dot5.value and dot6.value:
        print("Z")
    if backspace.value and not dot1.value and not dot2.value and not dot3.value and not dot4.value and not dot5.value and not dot6.value:
        print("backspace")