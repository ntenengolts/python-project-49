from random import randint


DESCRIPTION = 'What number is missing in the progression?'


def generate_progression(length, start, step):
    """
    Generates an arithmetic progression of a given length.

    Args:
        length (int): The number of elements in the progression.
        start (int): The starting number of the progression.
        step (int): The step (difference) between consecutive elements
            in the progression.

    Returns:
        list: A list of integers representing the arithmetic progression.
    """
    return [start + step * i for i in range(length)]


def generate_round():
    """
    Generates a question and the correct answer for the progression game.

    The question is an arithmetic progression with one missing term,
        and the answer is the missing term.

    Returns:
        tuple: A tuple containing the question as a string
            and the correct answer as a string.
    """
    length = randint(5, 10)
    start = randint(1, 10)
    step = randint(1, 10)
    progression = generate_progression(length, start, step)
    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer
