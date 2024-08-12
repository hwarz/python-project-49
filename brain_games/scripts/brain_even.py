#!/usr/bin/env python
import random
import prompt
from brain_games.cli import welcome_user


def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(1, 4):
        random_number = str(random.randint(1, 100))
        print(f'Question: {random_number}')
        answer = prompt.string(random_number)
        print(f'Your answer: {answer}')


if __name__ == '__main__':
    main()
