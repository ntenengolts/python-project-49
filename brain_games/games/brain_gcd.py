from random import randint
from brain_games.cli import welcome_user
import prompt


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_numbers():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    numbers = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return numbers, correct_answer


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    correct_answers = 0
    while correct_answers < 3:
        numbers, correct_answer = generate_numbers()
        print(f'Question: {numbers}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            correct_answers = 0

    print(f'Congratulations, {name}!')
