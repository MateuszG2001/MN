import unittest
from algorithms import *


class AlgorithmsTestCase(unittest.TestCase):
    def test_gaussian_elimination_if_num_of_rows_is_too_big_then_raises_exception(self):
        self.assertRaises(AlgorithmError, lambda: gaussian_elimination([[0]], 2))

    def test_gaussian_elimination_if_matrix_one_by_one_then_returns_unmodified_matrix(self):
        self.assertEqual([[0]], gaussian_elimination([[0]]))

    def test_gaussian_elimination_if_matrix_already_in_row_echelon_form_then_returns_unmodified_matrix(self):
        matrix = [
            [1, 0, -2, -3],
            [0, 1, 1, 4],
            [0, 0, 0, 0]
        ]
        self.assertEqual(matrix, gaussian_elimination(matrix))

    def test_gaussian_elimination_if_matrix_not_in_row_echelon_form_then_returns_correctly_transformed_matrix(self):
        matrix = [
            [1, 3, 1, 9],
            [1, 1, -1, 1],
            [3, 11, 5, 35]
        ]
        ret = gaussian_elimination(matrix)
        self.assertEqual(0, ret[1][0])
        self.assertEqual([0, 0, 0, 0], ret[2])

    def test_gaussian_elimination_if_called_then_the_original_matrix_is_unchanged(self):
        matrix = [
            [1, 3, 1, 9],
            [1, 1, -1, 1],
            [3, 11, 5, 35]
        ]
        self.assertNotEqual(matrix, gaussian_elimination(matrix))

    def test_gaussian_elimination_if_num_of_rows_is_less_than_max_then_returns_partially_transformed_matrix(self):
        matrix = [
            [3, 2, 1, -1, 0],
            [5, -1, 1, 2, -4],
            [1, -1, 1, 2, 4],
            [7, 8, 1, -7, 6]
        ]
        ret = gaussian_elimination(matrix)
        self.assertEqual(0, ret[1][0])
        self.assertEqual([0, 0], ret[2][0:2])
        self.assertNotEqual([0] * 5, ret[3])

    def test_solve_if_num_of_rows_is_too_big_then_raises_exception(self):
        matrix = [
            [1, 3, 1, 9],
            [1, 1, -1, 1],
            [3, 11, 5, 35]
        ]
        self.assertRaises(AlgorithmError, lambda: solve(matrix, gaussian_elimination, 22))

    def test_solve_if_matrix_one_by_one_then_raises_exception(self):
        self.assertRaises(AlgorithmError, lambda: solve([[0]], gaussian_elimination))

    def test_solve_if_matrix_is_inconsistent_then_raises_exception(self):
        matrix = [
            [1, 1, 1, 3],
            [1, 1, 1, 4]
        ]
        self.assertRaises(AlgorithmError, lambda: solve(matrix, gaussian_elimination))

    def test_solve_if_matrix_is_dependent_then_raises_exception(self):
        matrix = [
            [1, 1, 1, 3],
            [1, 1, 2, 4]
        ]
        self.assertRaises(AlgorithmError, lambda: solve(matrix, gaussian_elimination))

    def test_solve_if_matrix_is_determined_and_consistent_then_returns_correct_solution(self):
        matrix = [
            [1, 1, 3],
            [1, 2, 5]
        ]
        self.assertEqual([1, 2], solve(matrix, gaussian_elimination))

    def test_matrix_a(self):
        matrix = [
            [3, 3, 1, 12],
            [2, 5, 7, 33],
            [1, 2, 1, 8]
        ]
        self.assertEqual([1, 2, 3], solve(matrix, gaussian_elimination))

    def test_matrix_b(self):
        matrix = [
            [3, 3, 1, 1],
            [2, 5, 7, 20],
            [-4, -10, -14, -40]
        ]
        with self.assertRaises(AlgorithmError) as ctx:
            solve(matrix, gaussian_elimination)
            self.assertEquals(str(ctx.exception), 'The system of linear equations is dependent')

    def test_matrix_c(self):
        matrix = [
            [3, 3, 1, 1],
            [2, 5, 7, 20],
            [-4, -10, -14, -20]
        ]
        with self.assertRaises(AlgorithmError) as ctx:
            solve(matrix, gaussian_elimination)
            self.assertEquals(str(ctx.exception), 'The system of linear equations is inconsistent')

    def test_matrix_d(self):
        matrix = [
            [0.5, -0.0625, 0.1875, 0.0625, 1.5],
            [-0.0625, 0.5, 0, 0, -1.625],
            [0.1875, 0, 0.375, 0.125, 1],
            [0.0625, 0, 0.125, 0.25, 0.4375]
        ]
        expected = [2, -3, 1.5, 0.5]
        solution = solve(matrix, gaussian_elimination)
        for i in range(len(expected)):
            self.assertAlmostEqual(expected[i], solution[i])

    def test_matrix_e(self):
        matrix = [
            [3, 2, 1, -1, 0],
            [5, -1, 1, 2, -4],
            [1, -1, 1, 2, 4],
            [7, 8, 1, -7, 6]
        ]
        with self.assertRaises(AlgorithmError) as ctx:
            solve(matrix, gaussian_elimination)
            self.assertEquals(str(ctx.exception), 'The system of linear equations is inconsistent')

    def test_matrix_f(self):
        matrix = [
            [3, -1, 2, -1, -13],
            [3, -1, 1, 1, 1],
            [1, 2, -1, 2, 21],
            [-1, 1, -2, -3, -5]
        ]
        expected = [1, 3, -4, 5]
        solution = solve(matrix, gaussian_elimination)
        for i in range(len(expected)):
            self.assertAlmostEqual(expected[i], solution[i])

    def test_matrix_g(self):
        matrix = [
            [0, 0, 1, 3],
            [1, 0, 0, 7],
            [0, 1, 0, 5]
        ]
        self.assertEqual([7, 5, 3], solve(matrix, gaussian_elimination))

    def test_matrix_h(self):
        matrix = [
            [10, -5, 1, 3],
            [4, -7, 2, -4],
            [5, 1, 4, 19]
        ]
        self.assertEqual([1, 2, 3], solve(matrix, gaussian_elimination))

    def test_matrix_i(self):
        matrix = [
            [6, -4, 2, 4],
            [-5, 5, 2, 11],
            [0.9, 0.9, 3.6, 13.5]
        ]
        with self.assertRaises(AlgorithmError) as ctx:
            solve(matrix, gaussian_elimination)
            self.assertEquals(str(ctx.exception), 'The system of linear equations is dependent')

    def test_matrix_j(self):
        matrix = [
            [1, 0.2, 0.3, 1.5],
            [0.1, 1, -0.3, 0.8],
            [-0.1, -0.2, 1, 0.7]
        ]
        expected = [1, 1, 1]
        solution = solve(matrix, gaussian_elimination)
        for i in range(len(expected)):
            self.assertAlmostEqual(expected[i], solution[i])
