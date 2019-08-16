import braille
import time

while True:
    dots = braille.readDots()
    if dots in braille.dots_to_letter.keys():
        print(braille.dots_to_letter[dots])
    time.sleep(0.01)
    dots = braille.readDots()
    if dots in braille.dots_to_braille.keys():
        print(braille.dots_to_braille[dots])