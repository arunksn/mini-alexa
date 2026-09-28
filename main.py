"""Mini Alexa - a rule-based virtual assistant.

Flow: user input -> lowercase -> check keywords -> call a function -> respond.
No machine learning is used; commands are matched by simple keyword detection.

Run with:  python main.py
"""

import re
import sys

import ai_concepts
import calculator
import content
import datetime_utils
import game
import greetings
import help_menu

EXIT_WORDS = {"exit", "quit", "bye"}
HELP_WORDS = {"help"}
CALC_WORDS = {"calculate", "calculator", "calc"}
TIME_WORDS = {"time"}
DATE_WORDS = {"date"}
JOKE_WORDS = {"joke", "jokes"}
QUOTE_WORDS = {"quote", "quotes"}
FACT_WORDS = {"fact", "facts"}
GAME_WORDS = {"game", "games"}
RECOMMEND_WORDS = {"recommend", "recommendation", "recommendations"}
PERCEPTRON_WORDS = {"perceptron"}

FALLBACK_MESSAGE = "I'm not sure I understood that.\nType 'help' to see what I can do."


def detect_command(text):
    """Classify normalized (lowercase) input by keyword. Returns a command name."""
    words = set(re.findall(r"[a-z0-9']+", text))
    if not words:
        return "empty"

    # Order matters: the first matching group wins.
    checks = [
        ("exit", EXIT_WORDS),
        ("help", HELP_WORDS),
        ("calculate", CALC_WORDS),
        ("time", TIME_WORDS),
        ("date", DATE_WORDS),
        ("joke", JOKE_WORDS),
        ("quote", QUOTE_WORDS),
        ("fact", FACT_WORDS),
        ("game", GAME_WORDS),
        ("recommend", RECOMMEND_WORDS),
        ("perceptron", PERCEPTRON_WORDS),
        ("greeting", greetings.GREETING_WORDS),
    ]
    for command, keywords in checks:
        if words & keywords:
            return command
    return "unknown"


def extract_expression(text):
    """Return whatever follows the calculate keyword ('calculate 5 + 3' -> '5 + 3')."""
    match = re.search(r"\b(?:calculate|calculator|calc)\b(.*)$", text)
    return match.group(1).strip() if match else ""


def main():
    # Make sure symbols like the arrows in the help menu print on any terminal.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    print("=" * 32)
    print("          MINI ALEXA")
    print("=" * 32)

    name = "friend"   # used only if input ends before a name is given
    try:
        name = greetings.ask_name()
        greetings.say(greetings.welcome_message(name))

        while True:
            text = input("You: ").strip().lower()
            command = detect_command(text)

            if command == "exit":
                greetings.say(greetings.goodbye(name))
                break
            elif command == "empty":
                greetings.say("Please type a command. Type 'help' to see what I can do.")
            elif command == "help":
                print(help_menu.get_help_text())
                print()
            elif command == "calculate":
                greetings.say(calculator.run_calculator(extract_expression(text)))
            elif command == "time":
                greetings.say(datetime_utils.get_current_time())
            elif command == "date":
                greetings.say(datetime_utils.get_current_date())
            elif command == "joke":
                greetings.say(content.get_joke())
            elif command == "quote":
                greetings.say(content.get_quote())
            elif command == "fact":
                greetings.say(content.get_fact())
            elif command == "game":
                game.play_game(name)
            elif command == "recommend":
                greetings.say(ai_concepts.recommend())
            elif command == "perceptron":
                greetings.say(ai_concepts.perceptron_demo())
            elif command == "greeting":
                greetings.say(greetings.greet(name))
            else:
                greetings.say(FALLBACK_MESSAGE)
    except (EOFError, KeyboardInterrupt):
        # Ctrl+C / Ctrl+D / end of piped input: still exit gracefully.
        print()
        greetings.say(greetings.goodbye(name))


if __name__ == "__main__":
    main()
