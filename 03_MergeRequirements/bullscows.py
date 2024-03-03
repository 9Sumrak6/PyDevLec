import random
import sys
import urllib.request
import cowsay


word_len = 5

def my_cow(prompt):
    return(random.choice([f'/-_-\\ - *working*\n{prompt}', f'\\^_^/ - *watching anime*\n{prompt}']))


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
    #print(cowsay.cowsay(prompt, cow=cowsay.get_random_cow()))
    print(my_cow(prompt))
    while (inp := input()) not in valid or len(inp) != word_len:
        print(my_cow(prompt))
        #print(cowsay.cowsay(prompt, cow=cowsay.get_random_cow()))

    return inp


def inform(format_string: str, bulls: int, cows: int) -> None:
    print(cowsay.cowsay(format_string.format(bulls, cows), cow=cowsay.get_random_cow()))


def gameplay(ask: callable, inform: callable, words: list[str]) -> int:
    secret = ''

    while (secret := random.choice(words)) and len(secret) != word_len:
        pass

    print(secret)

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