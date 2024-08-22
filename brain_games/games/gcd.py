def gcd_gm():
    import random
    import prompt
    import math
    from brain_games.common_logic import common_code

    WhatToDoTextEven = 'Find the greatest common divisor of given numbers.'

    def gcd_game_code():
        random_number_1 = str(random.randint(1, 100))
        random_number_2 = str(random.randint(1, 100))
        print(f'Question: {random_number_1} {random_number_2}')
        correct_answer = str(
            math.gcd(int(random_number_1), int(random_number_2))
        )
        answer = prompt.string('Your answer: ')
        return answer, correct_answer

    common_code(gcd_game_code, WhatToDoTextEven)
