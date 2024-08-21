from brain_games.cli import welcome_user


def common_code(current_game_code, WhatToDoText):
    user_name = welcome_user()
    print(WhatToDoText)

    for i in range(3):
        answer, correct_answer = current_game_code()
        if answer == correct_answer:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {user_name}!')
                break
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was'
                  f' \'{correct_answer}\'.\nLet\'s try again, {user_name}!')
            break
