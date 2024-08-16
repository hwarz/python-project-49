#!/usr/bin/env python
import random
import prompt

from brain_games.cli import welcome_user


def main():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for i in range(3):
        random_number = str(random.randint(1, 100))
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if int(random_number)%2 == 0:
            correct_answer = 'yes' 
        if int(random_number)%2 == 1:
            correct_answer = 'no'
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
