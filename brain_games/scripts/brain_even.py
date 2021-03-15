#!/usr/bin/env python
from brain_games.games import brain_even
from brain_games import welcome_user


def main():
    name = welcome_user()
    brain_even.start_game(name)


if __name__ == '__main__':
    main()
