#!/usr/bin/env python
"""Starts brain-even game"""


from brain_games.games import brain_even
from ..engine import start_game


def main():
    start_game(brain_even)


if __name__ == '__main__':
    main()
