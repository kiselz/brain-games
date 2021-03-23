#!/usr/bin/env python
"""Starts brain-calc game"""


from brain_games.games import brain_calc
from ..engine import start_game


def main():
    start_game(brain_calc)


if __name__ == '__main__':
    main()
