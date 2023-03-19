import math
from textwrap import dedent

from algorithms import *
from function import *

functions = [
    Function(
        lambda x: x * (x * (x * (x + 1) - 14)) + 24,
        lambda x: x * (x * (4 * x + 3) - 28),
        -5, -1, "f(x) = x^4 + x^3 - 14x^2 +24"
    ),
    Function(
        lambda x: 2 ** x - math.sin(2 * x),
        lambda x: (math.log(2) * 2 ** x) - 2 * math.cos(2 * x),
        -4, 1, "g(x) = 2^x-sin(2x)"
    ),
    Function(
        lambda x: math.sin(x) + x - 1,
        lambda x: math.cos(x) + 1,
        -2, 2, "h(x) = sin(x)+x-1"
    ),
    Function(
        lambda x: 2 ** (math.sin(x) + x - 1) - math.sin(2 * (math.sin(x) + x - 1)),
        lambda x: 2 ** (math.sin(x) + x - 1) * math.log(2) * (math.cos(x) + 1) - 2 * math.cos(
            2 * (math.sin(x) + x - 1)) * (math.cos(x) + 1),
        -3, 1, "k(x) = 2^(six(x)+x-1)-sin(2*sin(x)+x-1)"
    )
]


def get_input(prompt, reader, predicate):
    ret = None
    try:
        ret = reader(prompt)
    except (IOError, ValueError):
        pass

    while not predicate(ret):
        try:
            ret = reader('Invalid input. Try again: ')
        except (IOError, ValueError):
            continue

    return ret


if __name__ == '__main__':
    print('Available functions:')
    for i in range(0, len(functions)):
        print(f'{i + 1}. {functions[i]}')

    f_choice = get_input(
        prompt='\nEnter your choice: ',
        reader=lambda m: int(input(m)) - 1,
        predicate=lambda v: v in range(0, len(functions))
    )

    functions[f_choice].plot()

    print(dedent("""
        Available end conditions:
        1. Reaching a fixed number of iterations
        2. |f(x)| <= ε
    """))

    e_choice = get_input(
        prompt='Enter your choice: ',
        reader=lambda m: int(input(m)),
        predicate=lambda v: v in range(1, 3)
    )

    end_condition = None
    if e_choice == 1:
        iterations = get_input(
            prompt='Enter the number of iterations: ',
            reader=lambda m: int(input(m)),
            predicate=lambda v: v > 0
        )
        end_condition = {'iterations': iterations}
    else:
        epsilon = get_input(
            prompt='Enter the value of ε: ',
            reader=lambda m: float(input(m)),
            predicate=lambda v: v > 0
        )
        end_condition = {'epsilon': epsilon}

    root = None
    iterations = None
    try:
        print('\n--- Bisection method ---')
        print('Specify interval')
        start = get_input(
            prompt='Start: ',
            reader=lambda m: float(input(m)),
            predicate=lambda v: True
        )
        end = get_input(
            prompt='End: ',
            reader=lambda m: float(input(m)),
            predicate=lambda v: True
        )
        root1, iterations1 = find_root_using_bisection_method(
            functions[f_choice],
            start,
            end,
            **end_condition)
        print('\n--- Newton method ---')
        guess = get_input(
            prompt='Enter initial guess: ',
            reader=lambda m: float(input(m)),
            predicate=lambda v: True
        )
        root2, iterations2 = find_root_using_newton_method(
            functions[f_choice],
            functions[f_choice].get_derivative(),
            guess,
            **end_condition)
    except AlgorithmError as e:
        print(e)
    else:
        functions[f_choice].plot([root1, root2], markers=[2, 3], colors=["red", "purple"])
        print('\n--- Results ---')
        print('Bisection method')
        print(f'Root approximation: {root1}')
        if not end_condition.get('iterations'):
            print(f'Iterations: {iterations1}')
        print('\nNewton method')
        print(f'Root approximation: {root2}')
        if not end_condition.get('iterations'):
            print(f'Iterations: {iterations2}')
