from random import randint
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name


def get_random_number(begin=0, end=100):
    return randint(begin, end)


def check_answer(answer, number):
    if answer == 'yes' and number % 2 == 0:
        return True
    if answer == 'no' and number % 2 != 0:
        return True
    return False


def reversed_answer(answer):
    return 'no' if answer == 'yes' else 'yes'


def even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    MAX_TRIES = 3
    curr_try = 0
    is_lost = False

    while curr_try < MAX_TRIES:
        curr_number = get_random_number()

        print('Question: {}'.format(curr_number))
        answer = input('Your answer: ')
        is_answer_right = check_answer(answer, curr_number)
        if is_answer_right:
            print('Correct!')
            curr_try += 1
        else:
            print("'{}' is wrong answer :(. Correct answer was '{}'"
                  .format(answer, reversed_answer(answer)))
            is_lost = True
            break
    if is_lost:
        print("Let's try again, {}".format(name))
    else:
        print('Congratulations, {}!'.format(name))
