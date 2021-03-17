from ..randomizer import get_random_number


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def start_game(name):
    MAX_TRIES = 3
    curr_try = 0
    is_lost = False

    while curr_try < MAX_TRIES:
        print('Find the greatest common divisor of given numbers.')

        number1, number2 = get_random_number(), get_random_number()

        right_answer = gcd(number1, number2)

        print('Question: {} {}'.format(number1, number2))

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
