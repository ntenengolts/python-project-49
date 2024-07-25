from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """
    Determines if number is prime.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if num is prime, False if isn't.
    """
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def generate_round():
    """
    Generates a question for the prime number game.

    Returns:
        tuple: A tuple containing the question as a string
            and the correct answer as a string.
    """
    num = randint(1, 100)
    question = str(num)
    correct_answer = 'yes' if is_prime(num) else 'no'
    return question, correct_answer
