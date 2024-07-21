from random import randint, choice
from brain_games.common import run_game


DESCRIPTION = 'What is the result of the expression?'


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    if num1 < num2:
        num1, num2 = num2, num1

    operator = choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    correct_answer = calculate(num1, num2, operator)
    return expression, str(correct_answer)


def main():
    run_game(DESCRIPTION, generate_round)
