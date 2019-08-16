# circuitpython-braille
Braille Keyboard made in CircuitPython

## Braille Keyboard Layout

![Circuit Playground, captouch pins](https://raw.githubusercontent.com/fede2cr/circuitpython-braille/master/imgs/circuitpython_TouchPads.jpg)

| Braille dot | On the Playground |
|-------------|-------------------|
| Dot 1       | A1                |
| Dot 2       | A2                |
| Dot 3       | A3                |
| Dot 4       | A4                |
| Dot 5       | A5                |
| Dot 6       | A6                |
| Backspace   | A7                |
| Keyboard active| CPX Switch     |

## Using via serial console

If you prefer, we can start with the Keyboard emulation turned off, by moving the switch no the CircuitPlayground Express to the Off position.

Now, get a serial console to read the output of the program. Please have in mind that the mu-editor [does not print unicode characters properly](https://github.com/mu-editor/mu/issues/797) so the braille character will not print properly.

## Using via keyboard emulation

To practice, get a text editor with a new document, and turn on keyboard emulation by making sure that the switch on the CircuitPlayground Express is set to On.

## How to write Braille

Get a braille table, from [the code](https://github.com/fede2cr/circuitpython-braille/blob/master/braille.py), from [Wikipedia](https://en.wikipedia.org/wiki/Braille) or from a [book](https://www.amazon.com/gp/product/1539368130/).

The easiest is the letter A. Just touch the pad labeled A1, and that is it.

For the letter B, press at the same time pad A1 and pad A2.

Letter C is **not** A1+A2+A3, but is actually just A1 with A4.

Now, how about trying to write your name using the table as reference?

## TODO

- Debounce.
- Add support for "indicators", used in numbers, uppercase and others.
- After indicators, add more characters.
