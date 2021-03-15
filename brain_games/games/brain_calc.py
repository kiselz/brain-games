from ..randomizer import get_random_number
from ..randomizer import get_random_element


def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2


def start_game(name):
    MAX_TRIES = 3
    curr_try = 0
    is_lost = False
    MATHEMATICAL_OPERATORS = ('+', '-', '*')

    while curr_try < MAX_TRIES:
        print('What is the result of the expression?')

        number1, number2 = get_random_number(), get_random_number()
        operator = get_random_element(MATHEMATICAL_OPERATORS)

        right_answer = calculate(number1, number2, operator)

        print('Question: {} {} {}'.format(number1, operator, number2))

        user_answer = int(input('Your answer: '))

        if user_answer == right_answer:
            print('Correct')
            curr_try += 1
        else:
            print("'{}' is wrong answer :(. Correct answer was '{}'"
                  .format(user_answer, right_answer))
            is_lost = True
            break

    if is_lost:
        print("Let's try again, {}".format(name))
    else:
        print('Congratulations, {}!'.format(name))
