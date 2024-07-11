from brain_games.cli import welcome_user
from random import randint
import prompt


def is_even(number):
    return number % 2 == 0


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answers = 0
    while correct_answers < 3:
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('You answer: ').strip().lower()

        correct_answer = 'yes' if is_even(number) else 'no'

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
