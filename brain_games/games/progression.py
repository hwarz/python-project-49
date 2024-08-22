def progression_gm():
    import random
    import prompt
    from brain_games.common_logic import common_code

    WhatToDoTextProgression = 'What number is missing in the progression?'

    def progression_game_code():
        progression_length = random.randint(5, 11)
        start = random.randint(1, 100)
        diff = random.randint(1, 20)
        progression = [start + j * diff for j in range(progression_length)]
        hidden_position = random.randint(0, progression_length - 1)
        correct_answer = str(progression[hidden_position])
        progression[hidden_position] = '..'
        progression = [str(_) for _ in progression]
        print(f'Question: {" ".join(progression)}')
        answer = prompt.string('Your answer: ')
        return answer, correct_answer

    common_code(progression_game_code, WhatToDoTextProgression)
