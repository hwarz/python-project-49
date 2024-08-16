#!/usr/bin/env python
import random
import prompt
import operator
import math

from brain_games.cli import welcome_user

def main():
    user_name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    #correct_answer = 'no'

    for i in range(3):
        random_number = str(random.randint(1, 100))
        print(f'Question: {random_number}')

        for j in range(2, (int(random_number) // 2 + 1)):
            if int(random_number) % j == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'

        if random_number == '1':
            correct_answer = 'no'
        if random_number == '2' or random_number == '3':
            correct_answer = 'yes'

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
