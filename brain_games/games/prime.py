#!/usr/bin/env python3.9
import random
import prompt
from brain_games.games.logic_prime import game_logic


def prime():
    print(
        "poetry run python -m brain_games.scripts."
        "brain_games\nWelcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(3):
        random_number = random.randrange(0, 1000)
        print(f"Question: {random_number}")

        answer = prompt.string("Your answer: ")

        if answer == game_logic(random_number):
            print("Correct!")
        else:
            print(
                f"Question: {random_number}"
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{game_logic(random_number)}'.\n Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
