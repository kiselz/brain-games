#!/usr/bin/env python
"""Starts brain-gcd game"""


from brain_games.games import brain_gcd
from ..engine import start_game


def main():
    start_game(brain_gcd)


if __name__ == '__main__':
    main()
