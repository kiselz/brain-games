#!/usr/bin/env python
from brain_games import even_game
from brain_games import welcome_user


def main():
    name = welcome_user()
    even_game(name)


if __name__ == '__main__':
    main()
