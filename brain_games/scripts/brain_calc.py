#!/usr/bin/env python
import random
import prompt
import operator

from brain_games.cli import welcome_user
operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]

def main():
    user_name = welcome_user()
    print('What is the rusult of the expression?')
    for i in range(1, 4):
        random_number_1 = str(random.randint(1, 100))
        random_number_2 = str(random.randint(1, 100))
        (random_math, random_operator) = random.choice(operators)
        print(f'Question: {random_number_1} {random_math} {random_number_2}')
        correct_answer = str(random_operator(int(random_number_1), int(random_number_2)))
        print(correct_answer)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        if answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{correct_answer}\'. Let\'s try again, {user_name}!')
            break

if __name__ == '__main__':
    main()
