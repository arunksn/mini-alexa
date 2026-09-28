"""Calculator feature: one operation between two numbers (+, -, *, /).

Bad input and division by zero never crash the assistant; they produce a
friendly message instead.
"""

import math
import re

_NUMBER = r"-?(?:\d+\.?\d*|\.\d+)"
_EXPRESSION = re.compile(rf"^({_NUMBER})\s*([+\-*/])\s*({_NUMBER})$")

INVALID_MESSAGE = (
    "I couldn't understand that calculation.\n"
    "Try something like: calculate 10 + 20\n"
    "I support + - * / between two numbers."
)


def format_number(value):
    """Format a result without float noise: 30.0 -> '30', 0.1+0.2 -> '0.3'."""
    text = f"{value:.6f}".rstrip("0").rstrip(".")
    return "0" if text in ("", "-0") else text


def calculate(expression):
    """Evaluate text such as '10 + 20' and return the assistant's reply."""
    cleaned = expression.strip().rstrip("=?").strip()
    match = _EXPRESSION.match(cleaned)
    if not match:
        return INVALID_MESSAGE

    left, operator, right = float(match.group(1)), match.group(2), float(match.group(3))
    if not (math.isfinite(left) and math.isfinite(right)):
        return "Those numbers are too large for me to handle."

    if operator == "+":
        result = left + right
    elif operator == "-":
        result = left - right
    elif operator == "*":
        result = left * right
    else:
        if right == 0:
            return "I can't divide by zero."
        result = left / right

    if not math.isfinite(result):
        return "That result is too large for me to handle."
    return f"The result is {format_number(result)}."


def run_calculator(expression=""):
    """Calculate `expression`; if it is empty, ask the user for one first."""
    if not expression.strip():
        expression = input("What would you like me to calculate? (e.g. 10 + 20): ")
    return calculate(expression)
