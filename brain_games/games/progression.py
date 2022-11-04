#!/usr/bin/env python3.9
import random
import prompt
from brain_games.games.logic_progression import game_logic


def progression():
    print("poetry run python -m brain_games.scripts.brain_games\nWelcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        iterator = random.randint(1, 10)
        result_list = game_logic(iterator)

        print(f"Question: {result_list}")

        answer = prompt.integer("Your answer: ")

        if answer == iterator:
            print("Correct!")
        else:
            print(
                f"Question: {result_list}"
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{iterator}'.\n Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
