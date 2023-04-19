import math

from function import *
from algorithms import *


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
    print('--- Functions ---')
    for i in range(0, len(functions)):
        print(f'{i + 1}. {functions[i]}')

    f_choice = get_input(
        prompt='\nEnter your choice: ',
        reader=lambda m: int(input(m)) - 1,
        predicate=lambda v: v in range(0, len(functions))
    )

    functions[f_choice].plot()
    plt.show()

    print('\n--- Interval ---')
    start = get_input(
        prompt=f'Start (>= {functions[f_choice].get_x_min()}): ',
        reader=lambda m: float(input(m)),
        predicate=lambda v: v >= functions[f_choice].get_x_min()
    )
    end = get_input(
        prompt=f'End (<= {functions[f_choice].get_x_max()}): ',
        reader=lambda m: float(input(m)),
        predicate=lambda v: v <= functions[f_choice].get_x_max()
    )

    print('\n--- Nodes ---')
    node_count = get_input(
        prompt='Enter number of nodes: ',
        reader=lambda m: int(input(m)),
        predicate=lambda v: v > 1
    )

    nodes_x = [start + i*((end - start) / (node_count - 1)) for i in range(0, node_count)]
    nodes_y = [functions[f_choice](x) for x in nodes_x]

    coefficient = divided_diff(nodes_x, nodes_y)[0, :]
    x = np.arange(functions[f_choice].get_x_min(), functions[f_choice].get_x_max() + .1, .1)
    y = newton_interpolation(coefficient, nodes_x, x)

    functions[f_choice].plot()
    plt.plot(x, y, dashes=[5, 5, 5, 5])
    plt.plot(nodes_x, nodes_y, 'bo')
    plt.show()
