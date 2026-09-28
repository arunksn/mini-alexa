"""Number guessing game: limited attempts with higher/lower hints."""

import random

from greetings import say

LOW = 1
HIGH = 20
MAX_ATTEMPTS = 5
_QUIT_WORDS = {"quit", "exit", "stop", "q"}


def play_game(name):
    """Play one round. Invalid guesses do not use up an attempt."""
    secret = random.randint(LOW, HIGH)
    say(
        f"Let's play, {name}! I'm thinking of a number between {LOW} and {HIGH}.\n"
        f"You have {MAX_ATTEMPTS} attempts. (Type 'quit' to give up.)"
    )

    attempts = 0
    while attempts < MAX_ATTEMPTS:
        raw = input("Guess: ").strip().lower()

        if raw in _QUIT_WORDS:
            say(f"Okay, leaving the game. The number was {secret}.")
            return

        try:
            guess = int(raw)
        except ValueError:
            say(f"Please enter a whole number between {LOW} and {HIGH}.")
            continue
        if not LOW <= guess <= HIGH:
            say(f"Please enter a number between {LOW} and {HIGH}.")
            continue

        attempts += 1
        if guess == secret:
            word = "attempt" if attempts == 1 else "attempts"
            say(f"Correct! You got it in {attempts} {word}, {name}!")
            return
        if attempts == MAX_ATTEMPTS:
            break
        left = MAX_ATTEMPTS - attempts
        hint = "Higher!" if guess < secret else "Lower!"
        say(f"{hint} ({left} {'attempt' if left == 1 else 'attempts'} left)")

    say(f"Out of attempts! The number was {secret}. Better luck next time!")
