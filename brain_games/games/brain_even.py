from ..randomizer import get_random_number


def check_answer(answer, number):
    if answer == 'yes' and number % 2 == 0:
        return True
    if answer == 'no' and number % 2 != 0:
        return True
    return False


def reversed_answer(answer):
    return 'no' if answer == 'yes' else 'yes'


def start_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    MAX_TRIES = 3
    curr_try = 0
    is_lost = False

    while curr_try < MAX_TRIES:
        curr_number = get_random_number()

        print('Question: {}'.format(curr_number))
        user_answer = input('Your answer: ')
        is_answer_right = check_answer(user_answer, curr_number)
        if is_answer_right:
            print('Correct!')
            curr_try += 1
        else:
            print("'{}' is wrong answer :(. Correct answer was '{}'"
                  .format(user_answer, reversed_answer(user_answer)))
            is_lost = True
            break
    if is_lost:
        print("Let's try again, {}".format(name))
    else:
        print('Congratulations, {}!'.format(name))
