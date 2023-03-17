import math
from textwrap import dedent

from algorithms import *
from function import *

functions = [
    Function(
        lambda x: x * (x * (x * x + 1) - 1) - 1,
        lambda x: x * (4 * x * x + 2) - 1,
        -2, 2, "f(x) = x^4 + x^2 - x - 1"
    ),
    Function(
        lambda x: x * (x * x - 1) + 1,
        lambda x: 3 * x * x - 1,
        -2, 2, "g(x) = x^3 - x + 1"
    ),
    Function(
        lambda x: -x * (x * (x - 2)) - 2,
        lambda x: -x * (3 * x - 4),
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
    try:
        print('\n--- Bisection method ---')
        print('Specify interval')
        start = float(input("Start: "))
        end = float(input("End: "))
        root1, iterations1 = find_root_using_bisection_method(
            functions[f_choice],
            start,
            end,
            **end_condition)
        print('\n --- Newton method ---')
        guess = float(input("Enter initial guess: "))
        root2, iterations2 = find_root_using_newton_method(
            functions[f_choice],
            functions[f_choice].get_derivative(),
            guess,
            **end_condition)
    except AlgorithmError as e:
        print(e)
    else:
        functions[f_choice].plot([root1],0)
        functions[f_choice].plot([root2],1)
        plt.show()
        print('\n--- Results ---')
        print('Bisection method')
        print(f'Root approximation: {root1}')
        if not end_condition.get('iterations'):
            print(f'Iterations: {iterations1}')
        print('\nNewton method')
        print(f'Root approximation: {root2}')
        if not end_condition.get('iterations'):
            print(f'Iterations: {iterations2}')
