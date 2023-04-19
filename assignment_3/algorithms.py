import numpy as np


def divided_diff(x, y):
    """
    A function to calculate the divided differences table
    
    :param x: A list of x-coordinates of the nodes
    :param y: A list of y-coordinates of the nodes
    :return: A divided differences table
    """

    n = len(y)
    coefficient = np.zeros([n, n])
    coefficient[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            coefficient[i][j] = (coefficient[i+1][j-1] - coefficient[i][j-1]) / (x[i+j] - x[i])

    return coefficient


def newton_interpolation(coefficient, nodes_x, x):
    """
    A function for evaluating the Newton polynomial at x

    :param coefficient: A divided differences table
    :param nodes_x: A list of x-coordinates of the nodes
    :param x: A list of x-coordinates at which the polynomial is calculated
    :return: A list of y-coordinates of the polynomial that is an interpolation of the nodes
    """

    n = len(nodes_x) - 1
    p = coefficient[n]
    for k in range(1, n + 1):
        p = coefficient[n-k] + p*(x - nodes_x[n - k])
    return p
