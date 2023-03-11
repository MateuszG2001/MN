import math
from textwrap import dedent

from algorithms import *
from function import *

functions = [
    Function(
        lambda x: x ** 4 + x ** 2 - x - 1,
        lambda x: 4 * x ** 3 + 2 * x - 1,
        -2, 2, "f(x) = x^4 + x^2 - x - 1"
    ),
    Function(
        lambda x: x ** 3 - x + 1,
        lambda x: 3 * x ** 2 - 1,
        -2, 2, "g(x) = x^3 - x + 1"
    ),
    Function(
        lambda x: 2 * x ** 2 - x ** 3 - 2,
        lambda x: 4 * x - 3 * x ** 2,
        -2, 3, "h(x) = 2x^2 - x^3 - 2"
    ),
    Function(
        lambda x: 2 ** x - 1,
        lambda x: 2 ** x * math.log(2),
        -1, 1, "k(x) = 2^x - 1"
    )
]

if __name__ == '__main__':
    print('Available functions:')
    for i in range(0, len(functions)):
        print(f'{i + 1}. {functions[i]}')

    f_choice = int(input('\nEnter your choice: '))
    while f_choice not in range(1, len(functions) + 1):
        f_choice = int(input('Invalid input. Try again: '))
    f_choice -= 1

    functions[f_choice].plot()

    print(dedent("""
        Available root finding methods:
        1. Bisection method
        2. Newton method"""))

    m_choice = int(input('\nEnter your choice: '))
    while m_choice not in range(1, 3):
        m_choice = int(input('Invalid input. Try again: '))

    print(dedent("""
        Available end conditions:
        1. Reaching a fixed number of iterations
        2. |f(x)| <= ε
    """))

    e_choice = int(input('Enter your choice: '))
    while e_choice not in range(1, 3):
        e_choice = int(input('Invalid input. Try again: '))

    end_condition = None
    if e_choice == 1:
        iterations = int(input('Enter the number of iterations: '))
        end_condition = {'iterations': iterations}
    else:
        epsilon = float(input('Enter the value of ε: '))
        end_condition = {'epsilon': epsilon}

    root = None
    iterations = None
    if m_choice == 1:
        print('\n--- Specify interval ---')
        start = float(input("Start: "))
        end = float(input("End: "))
        try:
            root, iterations = find_root_using_bisection_method(
                functions[f_choice],
                start,
                end,
                **end_condition)
        except Exception as e:
            print(e)
    elif m_choice == 2:
        guess = float(input("Enter initial guess: "))
        try:
            root, iterations = find_root_using_newton_method(
                functions[f_choice],
                functions[f_choice].get_derivative(),
                guess,
                **end_condition)
        except Exception as e:
            print(e)

    functions[f_choice].plot([root])

    if not end_condition.get('iterations'):
        print(f'\nIterations: {iterations}')
