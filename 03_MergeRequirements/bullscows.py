import random
import sys
import urllib.request


word_len = 5


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
    while (inp := input(prompt)) not in valid or len(inp) != word_len:
        pass

    return inp


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(format_string.format(bulls, cows))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = ''

    while (secret := random.choice(words)) and len(secret) != word_len:
        pass

    guess = ''
    tries = 0

    while guess != secret:
        bulls, cows = 0, 0

        guess = ask("Enter the word: ", words)
        cows, bulls = bullscows(guess, secret)
        inform("Bulls: {}, Cows: {}", bulls, cows)

        tries += 1

    return tries


if __name__ == "__main__":
    if len(sys.argv) not in [2, 3]:
        print("usage: python -m bullscows <dict_path> <word_len>")
        sys.exit(0)

    if len(sys.argv) == 3:
        word_len = int(sys.argv[2])

    dict_path = sys.argv[1]

    try:
        with urllib.request.urlopen(dict_path) as f:
            word_list = f.read().decode().split()
    except Exception:
        with open(dict_path) as f:
            word_list = f.read().split()

    print("Total attempts:", gameplay(ask, inform, word_list))