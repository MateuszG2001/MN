import matplotlib.pyplot as plt
from algorithms import *


def draw_function(func, roots, start, end, step, label):
    x = [i * step for i in range(int(1 / step) * start, int(1 / step) * end)]
    y = [func(i) for i in x]

    plt.axhline(0, color='black', linestyle='dashed')
    plt.plot(x, y)
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(label)
    plt.scatter(roots, [0 for _ in range(0, len(roots))], s=32, color="red")

    plt.show()


def f(x): return x ** 4 + x ** 2 - x - 1
def g(x): return x ** 3 - x + 1
def h(x): return 2 * x ** 2 - x ** 3 - 2
def dh(x): return 4 * x - 3 * x ** 2


draw_function(f, [find_root_using_bisection_method(f, -1, 0), find_root_using_bisection_method(f, 0.5, 1.5)],
              -2, 2, 0.001, "f(x) = x^4 + x^2 - x - 1")
draw_function(g, [find_root_using_bisection_method(g, -1.5, -1.0)], -2, 2, 0.001, "g(x) = x^3 - x + 1")
draw_function(h, [find_root_using_newton_method(h, dh, -1.5)], -2, 3, 0.001, "h(x) = 2 * x^2 - x^3 - 2")
