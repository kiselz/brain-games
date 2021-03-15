from random import randint
from random import choice


def get_random_number(begin=0, end=100):
    return randint(begin, end)


def get_random_element(iterable, begin=0, end=None):
    if end is None:
        end = len(iterable)

    return choice(iterable[begin:end])
