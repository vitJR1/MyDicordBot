from random import randrange


def flip():
    return randrange(2) == 0


def roll(min_value=0, max_value=100):
    return randrange(min_value, max_value + 1)
