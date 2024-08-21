def calc_gm():
    import random
    import prompt
    import operator
    from brain_games.common_logic import common_code
    WhatToDoTextCalc = 'What is the result of the expression?'
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]

    def calc_game_code():
        random_number_1 = str(random.randint(1, 100))
        random_number_2 = str(random.randint(1, 100))
        (random_math, random_operator) = random.choice(operators)
        print(f'Question: {random_number_1} {random_math} {random_number_2}')
        correct_answer = str(
            random_operator(int(random_number_1), int(random_number_2)))
        answer = prompt.string('Your answer: ')
        return answer, correct_answer

    common_code(calc_game_code, WhatToDoTextCalc)
