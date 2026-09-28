"""Date and time features, built on Python's datetime module."""

from datetime import datetime


def get_current_date(now=None):
    """Return a sentence with today's date, e.g. "Today's date is 27 August 2026."."""
    now = now or datetime.now()
    return f"Today's date is {now.day} {now.strftime('%B %Y')}."


def get_current_time(now=None):
    """Return a sentence with the current time, e.g. "The current time is 5:30 PM."."""
    now = now or datetime.now()
    clock = now.strftime("%I:%M %p").lstrip("0")   # 05:30 PM -> 5:30 PM
    return f"The current time is {clock}."
