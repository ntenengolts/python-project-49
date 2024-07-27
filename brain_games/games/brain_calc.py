from random import randint, choice


DESCRIPTION = 'What is the result of the expression?'


def calculate(num1, num2, operator):
    """
    Calculate the result of math expression.

    Args:
        num1 (int): The first number.
        num2 (int): The second number.
        operator (str): '+', '-' or '*'.

    Returns:
        int: The result of the expression.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2


def generate_round():
    """
    Generates a math expression (question) and correct answer.

    tuple: A tuple contain the expression as a string
        and the correct answer as a string.
    """
    num1 = randint(1, 100)
    num2 = randint(1, 100)

#    if num1 < num2:
#        num1, num2 = num2, num1

    operator = choice(['+', '-', '*'])
    expression = f'{num1} {operator} {num2}'
    correct_answer = calculate(num1, num2, operator)
    return expression, correct_answer
