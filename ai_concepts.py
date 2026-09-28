"""Simple demonstrations of AI ideas. No machine-learning model is trained.

1. A rule-based decision system (activity recommendation by time of day).
2. A perceptron - the basic building block of a neural network - done by hand.
"""

from datetime import datetime


# Rule-based recommendation

def get_time_of_day(hour):
    """Map an hour (0-23) to morning, afternoon, evening or night."""
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"


def recommend(now=None):
    """Recommend an activity using if/elif/else rules on the current time."""
    now = now or datetime.now()
    period = get_time_of_day(now.hour)

    if period == "morning":
        advice = "Have a healthy breakfast to start your day."
    elif period == "afternoon":
        advice = "It's time for a good lunch."
    elif period == "evening":
        advice = "Go for some exercise, like a walk or a workout."
    else:
        advice = "Get some rest. Sleep well!"

    return (
        f"It's {period}. {advice}\n"
        "(This is a rule-based decision: the current time picks the rule.)"
    )


# Perceptron 

def perceptron(inputs, weights, bias):
    """Return (weighted_sum, output) for a single perceptron.

    weighted_sum = (x1*w1) + (x2*w2) + ... + bias
    activation   = 1 if weighted_sum > 0 else 0
    """
    weighted_sum = sum(x * w for x, w in zip(inputs, weights)) + bias
    output = 1 if weighted_sum > 0 else 0
    return weighted_sum, output


def _fmt(value):
    """Show numbers cleanly (2.4000000000000004 -> 2.4, 1.0 -> 1)."""
    return format(round(value, 6), "g")


def perceptron_demo():
    """Explain a perceptron step by step with a fixed worked example."""
    inputs = [2, 3]
    weights = [0.5, 0.8]
    bias = 1

    products = [x * w for x, w in zip(inputs, weights)]
    weighted_sum, output = perceptron(inputs, weights, bias)

    lines = [
        "Perceptron demo (one artificial neuron, no training involved)",
        f"Inputs:  x1 = {inputs[0]}, x2 = {inputs[1]}",
        f"Weights: w1 = {weights[0]}, w2 = {weights[1]}",
        f"Bias:    {bias}",
        "",
        "Step 1 - Multiply each input by its weight:",
        f"  {inputs[0]} x {weights[0]} = {_fmt(products[0])}",
        f"  {inputs[1]} x {weights[1]} = {_fmt(products[1])}",
        "Step 2 - Add the results and the bias (the weighted sum):",
        f"  {_fmt(products[0])} + {_fmt(products[1])} + {bias} = {_fmt(weighted_sum)}",
        "Step 3 - Apply the activation function (if sum > 0 output 1, else 0):",
        f"  {_fmt(weighted_sum)} > 0, so the output is {output}"
        if output == 1
        else f"  {_fmt(weighted_sum)} is not > 0, so the output is {output}",
        "",
        "Concepts shown: input, weight, bias, weighted sum, activation function, output.",
    ]
    return "\n".join(lines)
