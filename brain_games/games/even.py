def even_gm():
    import random
    import prompt
    from brain_games.common_logic import common_code

    WhatToDoTextEven = \
        'Answer "yes" if the number is even, otherwise answer "no".'

    def even_game_code():
        random_number = str(random.randint(1, 100))
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if int(random_number) % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        return answer, correct_answer

    common_code(even_game_code, WhatToDoTextEven)
