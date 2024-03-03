def bullscows(guess: str, secret: str) -> (int, int):
    s = set(guess)

    cows, bulls = 0, 0

    for i, letter in enumerate(secret):
        if letter in s:
            if letter != guess[i]:
                cows += 1
            else:
                bulls += 1

    return (cows, bulls)

def gameplay(ask: callable, inform: callable, words: list[str]) -> int: