"""Predefined quotes, jokes and facts; one is picked at random on request."""

import random

QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Well done is better than well said. - Benjamin Franklin",
    "The best way to predict the future is to invent it. - Alan Kay",
    "The journey of a thousand miles begins with a single step. - Lao Tzu",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Small steps every day lead to big results.",
    "Every expert was once a beginner. Keep going!",
    "Mistakes are proof that you are trying.",
]

JOKES = [
    "Why did the developer go broke?\nBecause he used up all his cache!",
    "Why do programmers prefer dark mode?\nBecause light attracts bugs!",
    "Why was the computer cold?\nIt left its Windows open!",
    "How many programmers does it take to change a light bulb?\nNone, that's a hardware problem!",
    "Why did the programmer quit his job?\nBecause he didn't get arrays!",
    "What is a computer's favorite snack?\nMicrochips!",
    "Why do Python programmers wear glasses?\nBecause they can't C!",
    "What did the router say to the doctor?\nIt hurts when IP!",
    "Why was the math book sad?\nIt had too many problems.",
]

FACTS = [
    "Octopuses have three hearts.",
    "A day on Venus is longer than a year on Venus.",
    "Botanically speaking, bananas are berries but strawberries are not.",
    "The first computer 'bug' was a real moth found in a Harvard Mark II relay in 1947.",
    "The Python language is named after Monty Python's Flying Circus, not the snake.",
    "Water covers about 71% of the Earth's surface.",
    "An adult human body has 206 bones.",
    "Sunlight takes about 8 minutes to reach the Earth.",
    "Wombats produce cube-shaped droppings.",
    "Honey found in ancient Egyptian tombs was still safe to eat because honey barely spoils.",
]

_last_choice = {}


def _pick(category, items):
    """random.choice, re-drawn once so the same item never repeats back-to-back."""
    choice = random.choice(items)
    while len(items) > 1 and choice == _last_choice.get(category):
        choice = random.choice(items)
    _last_choice[category] = choice
    return choice


def get_quote():
    """Return a random motivational quote."""
    return _pick("quote", QUOTES)


def get_joke():
    """Return a random joke."""
    return _pick("joke", JOKES)


def get_fact():
    """Return a random fact."""
    return _pick("fact", FACTS)
