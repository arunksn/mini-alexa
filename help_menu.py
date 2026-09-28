"""Help menu listing every command Mini Alexa understands."""

HELP_TEXT = """========== MINI ALEXA ==========
time       → Show current time
date       → Show current date
calculate  → Perform calculation (e.g. calculate 10 + 20)
joke       → Tell a joke
quote      → Give motivational quote
fact       → Give random fact
game       → Play guessing game
recommend  → Get activity recommendation
perceptron → Run perceptron demo
help       → Show commands
exit       → Exit assistant (or type quit / bye)
================================"""


def get_help_text():
    """Return the help menu as a string."""
    return HELP_TEXT
