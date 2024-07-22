from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    return False


def generate_round():
    number = randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, str(correct_answer)
