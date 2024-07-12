from random import randint
from brain_games.common import run_game


DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(length, start, step):
    return [start + step * i for i in range(length)]


def generate_round():
    length = randint(5, 10)
    start = randint(1, 10)
    step = randint(1, 10)
    progression = generate_progression(length, start, step)
    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer


def main():
    run_game(DESCRIPTION, generate_round)
