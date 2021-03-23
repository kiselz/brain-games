from random import randint
from random import choice

DESCRIPTION = 'What is the result of the expression?'
MATHEMATICAL_OPERATORS = ('+', '-', '*')


def calculate_expression(number1, number2, operator):
    """Calculates given expression.
    Only '+', '-' and '*' operators are supported.

    Args:
        number1 int: First number
        number2 int: Second number
        operator str: '+' or '-' or '*'

    Returns:
        int: Result of the given expression
    """

    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2


def generate_round():
    number1, number2 = randint(0, 100), randint(0, 100)
    operator = choice(MATHEMATICAL_OPERATORS)

    question = 'Question: {} {} {}'.format(number1, operator, number2)
    right_answer = calculate_expression(number1, number2, operator)
    return question, right_answer
