from time import sleep

from morse.morse_data import char_space, code, dah, dit, dit_space, word_space
from utils.led import led_on


def dot():
    led_on(dit)
    sleep(dit_space)


def dash():
    led_on(dah)
    sleep(dit_space)


def morse_code(morse: list, repeat: int = 1):
    for rep in range(repeat):
        for char in morse:
            for symbol in char:
                if symbol == ".":
                    dot()
                elif symbol == "-":
                    dash()
                elif symbol == "/":
                    sleep(word_space - 2 * char_space)
        sleep(char_space)


def translate(word: str) -> list:
    return [code.get(char.upper(), "/") for char in word]