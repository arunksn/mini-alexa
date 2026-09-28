# Mini Alexa - Virtual AI Assistant

Mini Alexa is a small **rule-based** virtual assistant written in pure Python.
It reads what you type, looks for keywords, and calls the matching function.
**No machine-learning model is trained or used** - the project only *demonstrates*
AI/ML/DL ideas (a rule-based decision system and a perceptron) with simple Python.

## Requirements

- Python 3.8 or newer
- No third-party packages (standard library only: `datetime`, `random`, `re`, `math`, `sys`)

## How to run

```bash
cd virtual-ai-assistant
python main.py        # on some systems: python3 main.py
```

## Commands

| Command      | What it does                                             |
|--------------|----------------------------------------------------------|
| `hello`/`hi` | Greets you by name                                       |
| `time`       | Shows the current time (e.g. `5:30 PM`)                  |
| `date`       | Shows the current date (e.g. `27 August 2026`)           |
| `calculate`  | One calculation with `+ - * /`, e.g. `calculate 10 + 20` |
| `joke`       | Tells a random joke                                      |
| `quote`      | Gives a random motivational quote                        |
| `fact`       | Gives a random fact                                      |
| `game`       | Number guessing game (1-20, 5 attempts, higher/lower)   |
| `recommend`  | Recommends an activity based on the time of day          |
| `perceptron` | Step-by-step perceptron demonstration                    |
| `help`       | Shows the command list                                   |
| `exit` / `quit` / `bye` | Ends the program gracefully                   |

Typing `calculate` on its own makes the assistant ask for the calculation.
Anything it does not recognise gets a friendly reply, never a crash.

## Project structure

```
virtual-ai-assistant/
├── main.py            # main loop + keyword detection (request -> classify -> respond)
├── greetings.py       # asks and remembers the user's name; shared "Assistant:" output helper
├── datetime_utils.py  # current date and time (datetime module)
├── calculator.py      # + - * / with division-by-zero and invalid-input handling
├── content.py         # QUOTES, JOKES, FACTS lists + random.choice selection
├── game.py            # number guessing game
├── ai_concepts.py     # rule-based recommendation + perceptron demo
├── help_menu.py       # help text listing every command
└── README.md
```

## How it works

```
User input -> convert to lowercase -> check keywords -> find matching feature
           -> call function -> give response -> ask again
```

`main.py` normalises each input (`strip().lower()`), splits it into words and
checks them against keyword groups in a fixed order (`detect_command`). A plain
`if / elif / else` chain then calls the right function. If no keyword matches,
the fallback message is shown. The user's name is stored in a variable for the
whole session and reused in replies.

## AI concepts demonstrated

**1. Rule-based decision system (`recommend`)** - the current hour selects a rule:

| Time of day | Hours       | Recommendation |
|-------------|-------------|----------------|
| Morning     | 05:00-11:59 | Breakfast      |
| Afternoon   | 12:00-16:59 | Lunch          |
| Evening     | 17:00-20:59 | Exercise       |
| Night       | 21:00-04:59 | Rest           |

**2. Perceptron (`perceptron`)** - a single artificial neuron, the building block of
neural networks and deep learning. Worked example: inputs 2 and 3, weights 0.5 and
0.8, bias 1:

```
(2 x 0.5) + (3 x 0.8) + 1 = 4.4   ->   4.4 > 0   ->   output = 1
```

It shows the concepts: input, weight, bias, weighted sum, activation function, output.
Nothing is trained; the weights are fixed values chosen for the demonstration.

## Sample session

```
Assistant: Hi! I'm Mini Alexa. What's your name?
You: Arun
Assistant: Nice to meet you, Arun!
           What can I do for you?
You: calculate 10 / 0
Assistant: I can't divide by zero.
You: calculate 10 + 20
Assistant: The result is 30.
You: joke
Assistant: Why do programmers prefer dark mode?
           Because light attracts bugs!
You: tell me about football
Assistant: I'm not sure I understood that.
           Type 'help' to see what I can do.
You: bye
Assistant: Goodbye, Arun! Have a great day.
```

## Testing performed

- Calculator: all four operators, decimals, negatives, spacing variations,
  division by zero (`10 / 0`, `0 / 0`), invalid text, incomplete expressions, huge numbers.
- Time and date output checked against fixed dates (including 12:00 AM/PM and single-digit days).
- Recommendation checked at every time-of-day boundary (04:xx, 05:00, 11:59, 12:00, 16:59, 17:00, 20:59, 21:00).
- Perceptron checked for output 1, output 0, and a weighted sum of exactly 0.
- Guessing game: win, loss, hints, invalid or out-of-range guesses (these do not use up attempts), quitting early.
- Jokes/quotes/facts: always come from the lists, never the same item twice in a row.
- Unknown input, empty input, empty name, `exit`/`quit`/`bye`, and Ctrl+C / Ctrl+D all end or continue without errors.

## Limitations

- Commands are matched by keywords, so the assistant does not understand free-form sentences.
- The calculator handles one operation between two numbers (e.g. `12 * 3`), not chained expressions.
- Nothing is saved after the program closes; the name is remembered only for the current session.
