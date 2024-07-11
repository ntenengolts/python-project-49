from random import randint
from brain_games.cli import welcome_user
import prompt


def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('You answer: ').strip().lower()

        correct_answer = 'yes' if is_prime(number) else 'no'

        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            correct_answers = 0

    print(f'Congratulations, {name}!')
