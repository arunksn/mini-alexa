"""Greeting feature: ask the user's name, remember it, and use it later.

Also holds the shared `say` helper that prints every assistant message with
the same "Assistant:" prefix, so all modules speak with one consistent voice.
"""

import re

GREETING_WORDS = {"hello", "hi", "hey", "greetings"}
_PREFIX = "Assistant: "

# Phrases people often type before their name ("my name is Arun").
_NAME_LEAD_IN = re.compile(
    r"^(my name is|i am|i'm|call me|this is|it's|its)\s+", re.IGNORECASE
)


def say(message):
    """Print an assistant message; continuation lines are aligned under the first."""
    lines = str(message).split("\n")
    print(_PREFIX + lines[0])
    for line in lines[1:]:
        print((" " * len(_PREFIX) + line) if line else "")
    print()


def clean_name(raw):
    """Tidy the raw text typed as a name. Returns '' if nothing usable remains."""
    name = " ".join(raw.split())          # trim and collapse extra spaces
    name = _NAME_LEAD_IN.sub("", name).strip(" .!,")
    if name and name == name.lower():     # "Arun" -> "Arun"
        name = name.title()
    return name


def ask_name():
    """Ask for the user's name until a non-empty one is given, and return it."""
    say("Hi! I'm Mini Alexa. What's your name?")
    while True:
        name = clean_name(input("You: "))
        if name:
            return name
        say("I didn't catch that. What's your name?")


def welcome_message(name):
    """Message shown right after the name is stored."""
    return f"Nice to meet you, {name}!\nWhat can I do for you?"


def greet(name):
    """Reply to 'hello', 'hi', etc. using the remembered name."""
    return f"Hello {name}!"


def goodbye(name):
    """Farewell message used when the user exits."""
    return f"Goodbye, {name}! Have a great day."
