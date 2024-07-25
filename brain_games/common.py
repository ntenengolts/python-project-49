import prompt


def welcome_user():
    """
    Greets the user and prompts them to enter their name.

    Prints a welcome message and asks for the user's name,
        then greets the user by name.

    Returns:
        str: The name of the user.
    """
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run_game(game):
    """
    Runs a game session.

    The game session includes greeting the user,
    displaying the game description,
    asking questions, checking answers,
    and tracking the number of correct answers.
    The game ends after three correct answers or one incorrect answer.

    Args:
        game (module): The game module which contains DESCRIPTION
            and generate_round function.
    """
    name = welcome_user()
    print(game.DESCRIPTION)
    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = game.generate_round()
        print(f'Question: {question}')
        answer = prompt.string('You answer: ').strip().lower()

        if answer == str(correct_answer):
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
