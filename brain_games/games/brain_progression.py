from random import randint
from brain_games.cli import welcome_user
import prompt


def generate_progression(length, start, step):
    progression = [start + step * i for i in range(length)]
    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    correct_answers = 0
    while correct_answers < 3:
        length = randint(5, 10)
        start = randint(1, 10)
        step = randint(1, 10)
        question, correct_answer = generate_progression(length, start, step)
        print(f'Question: {question}')
        answer = prompt.string('You answer: ')

        if answer == str(correct_answer):
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
