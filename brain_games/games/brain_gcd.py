from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    """Returns the greatest common divisor of a and b

    Args:
        a int: First number
        b int: Second numer

    Returns:
        int: greatest common divisor of a and b
    """
    while b != 0:
        a, b = b, a % b
    return a


def generate_round():
    """Generates the round for brain-gcd game

    Returns:
        Randomized question and right answer to it
    """
    number1, number2 = randint(1, 100), randint(1, 100)

    question = 'Question: {} {}'.format(number1, number2)
    right_answer = gcd(number1, number2)
    return question, right_answer
