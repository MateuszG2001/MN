import csv
from algorithms import *


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


def get_input_from_file(prompt):
    ret = None
    while True:
        try:
            filename = input(prompt)

            with open(filename, 'r') as file:
                reader = csv.reader(file, delimiter=';')
                ret = [[float(v) for v in row] for row in list(reader)]
        except Exception as e:
            print(e)
            continue
        else:
            break

    return ret


if __name__ == '__main__':

    matrix = get_input_from_file(
        prompt="Enter the name of the file containing the equations: "
    )

    # Print the matrix
    print('\n--- MATRIX ---')
    s = [[str(e) for e in row] for row in matrix]
    lens = [max(map(len, col)) for col in zip(*s)]
    fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
    table = [fmt.format(*row) for row in s]
    print('\n'.join(table))

    num_of_rows = get_input(
        prompt="\nEnter the number of equations (if all enter 0): ",
        reader=lambda m: int(input(m)),
        predicate=lambda v: v is not None
    )
    if num_of_rows == 0:
        num_of_rows = None

    try:
        print(f'\n--- SOLUTION ---\n{solve(matrix, gaussian_elimination, num_of_rows)}')
    except Exception as e:
        print(e)
