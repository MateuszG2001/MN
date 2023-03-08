import unittest
from algorithms import *


class MyTestCase(unittest.TestCase):
    def test_find_root_using_bisection_method_if_both_epsilon_and_iterations_where_provided_then_raises_exception(self):
        self.assertRaises(Exception, lambda: find_root_using_bisection_method(lambda x: x, -2, 2, epsilon=0.1, iterations=22))

    def test_find_root_using_bisection_method_if_the_func_vals_do_not_have_diff_signs_at_the_ends_of_the_intervals_then_raises_exception(self):
        self.assertRaises(Exception, lambda: find_root_using_bisection_method(lambda x: x**2, -2, 2))

    def test_find_root_using_bisection_method_if_valid_params_and_epsilon_provided_exists_then_returns_approx_of_root(self):
        self.assertAlmostEqual(-1.3247, find_root_using_bisection_method(lambda x: x**3 - x + 1, -2, 2, epsilon=0.1), 1)

    def test_find_root_using_bisection_method_if_valid_params_and_iterations_provided_exists_then_returns_approx_of_root(self):
        self.assertAlmostEqual(-0.56984, find_root_using_bisection_method(lambda x: x**4 + x**2 - x - 1, -1, 0, iterations=10), 1)


if __name__ == '__main__':
    unittest.main()
