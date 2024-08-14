#!/usr/bin/env python
import random
import prompt
from brain_games.cli import welcome_user


def main():
    # welcome_user()
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(1, 4):
        random_number = str(random.randint(1, 100))
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        # print(f'Your answer: {answer}')
        # print(int(random_number)%2)
        # if int(random_number)%2 == 0 and answer == 'yes':
        if int(random_number)%2 == 0:
            correct_answer = 'yes' 
        if int(random_number)%2 == 1:
            correct_answer = 'no'
        if answer == correct_answer:
            print('Correct!')
        if i == 3:
            print(f'Congratulations, {user_name}')
            break 
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'. Let\'s try again, {user_name}!')
            break

if __name__ == '__main__':
    main()
