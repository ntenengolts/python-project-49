from random import randint, choice
from brain_games.cli import welcome_user
import prompt


def generate_expression():
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    if num1 < num2:
        num1, num2 = num2, num1

    operator = choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    elif operator == '*':
        correct_answer = num1 * num2
    return expression, str(correct_answer)


def main():
    name = welcome_user()
    print('What is the result of the expression?')
    correct_answers = 0
    while correct_answers < 3:
        expression, correct_answer = generate_expression()
        print(f'Question: {expression}')
        answer = prompt.string('Your answer: ')

        if answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            correct_answers = 0

    print(f'Congratulations, {name}!')
