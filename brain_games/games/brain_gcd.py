from random import randint
from brain_games.common import run_game


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_round():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    numbers = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return numbers, str(correct_answer)


def main():
    run_game(globals())
