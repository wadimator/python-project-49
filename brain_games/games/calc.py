#!/usr/bin/env python3.9
import random
import prompt
from brain_games.games.logic_calc import game_logic


def calc():
    print("poetry run python -m brain_games.scripts.brain_games\nWelcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print('What is the result of the expression?')
    for i in range(3):
        random_number1 = random.randrange(0, 100)
        random_number2 = random.randrange(0, 100)
        list_characters = ["+", "-", "*"]
        random_character = random.choice(list_characters)
        print(f"Question: {random_number1} {random_character} {random_number2}")

        answer = prompt.integer("Your answer: ")

        correct_answer = game_logic(random_number1, random_number2, random_character)
        if answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"Question: {random_number1} {random_character} {random_number2}"
                f"'{answer}' is wrong answer ;(. Correct answer was "
                f"'{correct_answer}'.\n Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
