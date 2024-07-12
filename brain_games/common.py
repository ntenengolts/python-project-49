import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name


def run_game(description, generate_round):
    name = welcome_user()
    print(description)
    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = generate_round()
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
