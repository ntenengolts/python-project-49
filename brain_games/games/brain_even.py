from random import randint
from brain_games.common import run_game


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    number = randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return question, correct_answer


def main():
    run_game(DESCRIPTION, generate_round)
