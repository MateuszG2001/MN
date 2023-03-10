import math

from algorithms import *
from function import *

f = Function(lambda x: x ** 4 + x ** 2 - x - 1, lambda x: 4 * x ** 3 + 2 * x - 1, -2, 2, "f(x) = x^4 + x^2 - x - 1")
g = Function(lambda x: x ** 3 - x + 1, lambda x: 3 * x ** 2 - 1, -2, 2, "g(x) = x^3 - x + 1")
h = Function(lambda x: 2 * x ** 2 - x ** 3 - 2, lambda x: 4 * x - 3 * x ** 2, -2, 3, "h(x) = 2 * x^2 - x^3 - 2")
k = Function(lambda x: 2 ** x - 1, lambda x: 2 ** x * math.log(2), -1, 1, "k(x) = 2^x - 1")

f.plot([find_root_using_bisection_method(f, -1, 0), find_root_using_bisection_method(f, 0.5, 1.5)])
g.plot([find_root_using_bisection_method(g, -1.5, -1.0)])
h.plot([find_root_using_newton_method(h, h.get_derivative(), -1.5)])
k.plot([find_root_using_newton_method(k, k.get_derivative(), 2)])
