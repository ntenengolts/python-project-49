from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    """
    Calculates the greatest common divisor of two numbers
        using the Euclidean algorithm.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The GCD of the two numbers.
    """
    while b:
        a, b = b, a % b
    return a


def generate_round():
    """
    Generates a question and the correct answer for the GCD game.

    The question is a pair of random integers,
        and the answer is their greatest common divisor.

    Returns:
        tuple: A tuple containing the question as a string
            and the correct answer as a string.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)

    numbers = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return numbers, correct_answer
