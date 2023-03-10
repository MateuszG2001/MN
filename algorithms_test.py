import unittest
from algorithms import *


class MyTestCase(unittest.TestCase):
    def test_find_root_using_bisection_method_if_both_epsilon_and_iterations_where_provided_then_raises_exception(self):
        self.assertRaises(Exception, lambda: find_root_using_bisection_method(lambda x: x, -2, 2, epsilon=0.1, iterations=22))

    def test_find_root_using_bisection_method_if_the_func_vals_do_not_have_diff_signs_at_the_ends_of_the_interval_then_raises_exception(self):
        self.assertRaises(Exception, lambda: find_root_using_bisection_method(lambda x: x**2, -2, 2))

    def test_find_root_using_bisection_method_if_valid_params_and_epsilon_provided_exists_then_returns_approx_of_root(self):
        self.assertAlmostEqual(-1.3247, find_root_using_bisection_method(lambda x: x**3 - x + 1, -2, 2, epsilon=0.1), 1)

    def test_find_root_using_bisection_method_if_valid_params_and_iterations_provided_exists_then_returns_approx_of_root(self):
        self.assertAlmostEqual(-0.56984, find_root_using_bisection_method(lambda x: x**4 + x**2 - x - 1, -1, 0, iterations=10), 1)

    def test_find_root_using_newton_method_if_both_epsilon_and_iterations_where_provided_then_raise_exception(self):
        self.assertRaises(Exception, lambda: find_root_using_newton_method(lambda x: x, lambda dx: 1, -2, epsilon=0.1, iterations=22))

    # If the function has the same sign on both sides of the root, then its second derivative changes sign, which means
    # that one of the requirements for applying Newton's method is not met.
    def test_find_root_using_newton_method_if_the_func_vals_do_not_have_diff_signs_on_both_sides_of_root_then_raises_exception(self):
        self.assertRaises(Exception, lambda: find_root_using_newton_method(lambda x: x**2, lambda x: 0.5*x, -2))

    def test_find_root_using_newton_method_if_valid_params_and_epsilon_provided_exists_then_returns_approx_of_root(self):
        self.assertAlmostEqual(-1.3247, find_root_using_newton_method(lambda x: x**3 - x + 1, lambda x: 3*x**2 - 1, -2, epsilon=0.1), 1)

    def test_find_root_using_newton_method_if_valid_params_and_iterations_provided_exists_then_returns_approx_of_root(self):
        self.assertAlmostEqual(-0.56984, find_root_using_newton_method(lambda x: x**4 + x**2 - x - 1, lambda x: 4*x**3 + 2*x - 1, -1, iterations=10), 1)

    def test_find_root_using_newton_method_if_function_has_local_extremum_between_initial_guess_end_root_then_raises_exception(self):
        self.assertRaises(Exception, lambda: find_root_using_newton_method(lambda x: 2*x^2-x**3-2, lambda x: 4*x - 3*x**2, 1, epsilon=0.1))


if __name__ == '__main__':
    unittest.main()
