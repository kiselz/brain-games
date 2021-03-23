from random import randint

DESCRIPTION = "Answer 'yes' if the number is even otherwise answer 'no'"


def generate_round():
    number = randint(0, 100)

    question = 'Question: {}'.format(number)
    return question, 'yes' if number % 2 == 0 else 'no'
