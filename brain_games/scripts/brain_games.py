#!/usr/bin/env python3.9
from brain_games.games.games import game
from brain_games.cli import welcome_user


def main():
    game()
    welcome_user()


if __name__ == '__main__':
    main()
