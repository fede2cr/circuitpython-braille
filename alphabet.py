"""
Dots 1-6, backspace, space and enter
"""
dots_to_alphabet = {
    # a-z
    0b100000000: { 'latin': "a", 'braille': '⠁'},
    0b110000000: { 'latin': "b", 'braille': '⠃'},
    0b100100000: { 'latin': "c", 'braille': '⠉'},
    0b100110000: { 'latin': "d", 'braille': '⠙'},
    0b100010000: { 'latin': "e", 'braille': '⠑'},
    0b110100000: { 'latin': "f", 'braille': '⠋'},
    0b110110000: { 'latin': "g", 'braille': '⠛'},
    0b110010000: { 'latin': "h", 'braille': '⠓'},
    0b010100000: { 'latin': "i", 'braille': '⠊'},
    0b010110000: { 'latin': "j", 'braille': '⠚'},
    0b101000000: { 'latin': "k", 'braille': '⠅'},
    0b111000000: { 'latin': "l", 'braille': '⠇'},
    0b101100000: { 'latin': "m", 'braille': '⠍'},
    0b101110000: { 'latin': "n", 'braille': '⠍'},
    0b101010000: { 'latin': "o", 'braille': '⠕'},
    0b111100000: { 'latin': "p", 'braille': '⠕'},
    0b111110000: { 'latin': "q", 'braille': '⠟'},
    0b111010000: { 'latin': "r", 'braille': '⠗'},
    0b011100000: { 'latin': "s", 'braille': '⠗'},
    0b011110000: { 'latin': "t", 'braille': '⠞'},
    0b101001000: { 'latin': "u", 'braille': '⠥'},
    0b111001000: { 'latin': "v", 'braille': '⠧'},
    0b010111000: { 'latin': "w", 'braille': '⠺'},
    0b101101000: { 'latin': "x", 'braille': '⠭'},
    0b101111000: { 'latin': "y", 'braille': '⠽'},
    0b101011000: { 'latin': "z", 'braille': '⠵'},
    # Simples: characters with only one block
    0b000000010: { 'latin': " ", 'braille': ' '},
    0b000000001: { 'latin': "\n", 'braille': '\n'},
    0b001000000: { 'latin': "'", 'braille': '⠄'},
    0b011000000: { 'latin': ";", 'braille': '⠆'},
    0b010010000: { 'latin': ":", 'braille': '⠒'},
    0b010000000: { 'latin': ",", 'braille': '⠂'},
    0b011010000: { 'latin': "!", 'braille': '⠖'},
    0b001001000: { 'latin': "-", 'braille': '⠤'},
    0b010011000: { 'label': ".", 'braille': '⠲'},
    0b011001000: { 'label': "?", 'braille': '⠦'},
    # Special and indicators: characters that are defined by two or more blocks
    0b000001000: { 'latin': 'capital indicator', 'braille': '⠠'}, # only one: capital letter indicator, times 2: capital word, times 3: capital passage
    0b001111000: { 'latin': 'number', 'braille': '⠼'},
    0b000000100: { 'latin': "backspace", 'braille': ''},
}