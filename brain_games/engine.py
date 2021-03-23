from .cli import welcome_user


def start_game(game):
    """Start games

    Args:
        game: Python module
    """

    print('Welcome to the Brain Games!')
    player_name = welcome_user()

    print(game.DESCRIPTION)

    MAX_TRIES = 3
    curr_try = 0
    is_lost = False

    while curr_try < MAX_TRIES:
        question, right_answer = game.generate_round()
        print(question)
        player_answer = input('Your answer: ')

        if player_answer == right_answer:
            print('Correct!')
            curr_try += 1
        else:
            print("'{}' is wrong answer :(. Correct answer was '{}'"
                  .format(player_answer, right_answer))
            is_lost = True
            break

    if is_lost:
        print("Let's try again, {}".format(player_name))
    else:
        print('Congratulations, {}!'.format(player_name))
