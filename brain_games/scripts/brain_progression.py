#!/usr/bin/env python
import random
import prompt
import operator
import math

from brain_games.cli import welcome_user

def main():
    user_name = welcome_user()
    print('What number is missing in the progression?')

    for i in range(3):
        progression_length = random.randint(5, 11)
        start = random.randint(1, 100) 
        diff = random.randint(1, 20)
        progression = [start + j * diff for j in range(progression_length)]
        hidden_position = random.randint(0, progression_length - 1)
        correct_answer = str(progression[hidden_position])
        print(correct_answer)
        progression[hidden_position] = '..'
        progression = [str(_) for _ in progression]
        print(f'Question: {" ".join(progression)}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {user_name}!')
                break
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'.\nLet\'s try again, {user_name}!')
            break

if __name__ == '__main__':
    main()
