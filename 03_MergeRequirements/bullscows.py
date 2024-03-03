import random
import sys
import urllib.request


def bullscows(guess: str, secret: str) -> (int, int):
    s = set(secret)

    cows, bulls = 0, 0

    for i, letter in enumerate(guess):
        if letter in s:
            if i < len(secret) and letter == secret[i]:
                bulls += 1
            else:
                cows += 1

    return (cows, bulls)


def ask(prompt: str, valid: list[str] = None) -> str:
    while (inp := input(prompt)) not in valid:
        pass

    return inp


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = random.choice(words)
    guess = ''
    tries = 0

    print(secret)

    while guess != secret:
        bulls, cows = 0, 0

        guess = ask("Enter the word: ", words)
        cows, bulls = bullscows(guess, secret)
        inform("Bulls: {}, Cows: {}", bulls, cows)

        tries += 1

    return tries


print(gameplay(ask, inform, ['lala', 'lalala', 'la', 'lalalalala', 'lalalalalalalala']))