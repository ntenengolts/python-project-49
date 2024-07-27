from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    """
    Determines if a number is even.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is even, Fals otherwise.
    """
    if number % 2 == 0:
        return True
    return False


def generate_round():
    """
    Generates a question for the even number game.

    Returns:
        tuple: A tuple containing the question as a string
            and the correct answer as a string.
    """
    number = randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
