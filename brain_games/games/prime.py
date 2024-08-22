def prime_gm():
    import random
    import prompt
    from brain_games.common_logic import common_code

    WhatToDoTextPrime = \
        'Answer "yes" if given number is prime. Otherwise answer "no".'

    def prime_game_code():
        random_number = str(random.randint(1, 100))
        print(f'Question: {random_number}')
        correct_answer = 'yes'
        if int(random_number) > 3:
            for j in range(2, (int(random_number) // 2 + 1)):
                if int(random_number) % j == 0:
                    correct_answer = 'no'
                    break
                else:
                    correct_answer = 'yes'
        if int(random_number) == 1:
            correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        return answer, correct_answer

    common_code(prime_game_code, WhatToDoTextPrime)
