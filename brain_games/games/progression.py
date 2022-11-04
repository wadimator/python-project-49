#!/usr/bin/env python3.9
import prompt
from brain_games.games.logic_progression import game_logic


def progression():
    print("poetry run python -m brain_games.scripts.brain_games\nWelcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print('Find the greatest common divisor of given numbers.')
    for i in range(3):
        result_list, result_number = game_logic()

        print("Question: ", *result_list)

        answer = prompt.integer("Your answer: ")

        if answer == result_number:
            print("Correct!")
        else:
            print(
                f"\n'{answer}' is wrong answer ;(. Correct answer was "
                f"'{result_number}'.\n Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
