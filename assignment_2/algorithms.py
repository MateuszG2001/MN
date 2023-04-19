import copy


class AlgorithmError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


def gaussian_elimination(matrix, num_of_rows=None):
    """
    Transforms the given matrix into a matrix in row-echelon form, i.e. a matrix having the following properties:

        - All rows consisting of only zeros are at the bottom.
        - The leading entry (that is the left-most nonzero entry) of every nonzero row is to the right of the leading
          entry of every row above.

    :param matrix: The matrix to be transformed into row-echelon form. The transformation is performed not-in-place.
    :param num_of_rows: Optional parameter specifying the number of rows to be transformed.
    In other words, the input matrix is treated as if it has only num_of_rows rows.
    If the value of this parameter is greater than the number of rows in the given matrix, an exception is raised.
    By default, all rows are transformed.
    :return: Returns the transformed matrix
    """
    matrix = copy.deepcopy(matrix)

    if num_of_rows is None:
        num_of_rows = len(matrix)
    elif num_of_rows > len(matrix):
        raise AlgorithmError('The given number of rows is too big')

    num_of_cols = len(matrix[0])

    pivot_row = 0
    pivot_col = 0

    while pivot_row < num_of_rows and pivot_col < num_of_cols:
        pivot_index = pivot_row
        for i in range(pivot_row + 1, num_of_rows):
            if abs(matrix[i][pivot_col]) > abs(matrix[pivot_index][pivot_col]):
                pivot_index = i

        if matrix[pivot_index][pivot_col] == 0:
            # No pivot in this column, pass to next column
            pivot_col += 1
        else:
            matrix[pivot_row], matrix[pivot_index] = matrix[pivot_index], matrix[pivot_row]
            for i in range(pivot_row + 1, num_of_rows):
                f = matrix[i][pivot_col] / matrix[pivot_row][pivot_col]

                # Fill with zeros the lower part of pivot column
                matrix[i][pivot_col] = 0

                for j in range(pivot_col + 1, num_of_cols):
                    matrix[i][j] -= f * matrix[pivot_row][j]

            pivot_row += 1
            pivot_col += 1

    return matrix


def solve(matrix, transformer, num_of_rows=None, epsilon=0.00001):
    """
    Solves the given system of linear equations using the given transformer to transform the matrix into a matrix in
    row-echelon form. If the system of linear equations is inconsistent (it has no solution) or is dependent (it has
    infinitely many solutions) then an exception is raised.

    :param matrix: A system of linear equations
    :param transformer: A function that transforms the given matrix into a matrix in row-echelon form
    :param num_of_rows: Optional parameter specifying the number of rows of the matrix to be considered when solving
    the system of linear equations.
    If the value of this parameter is greater than the number of rows in the given matrix, an exception is raised.
    By default, all rows are evaluated.
    :param epsilon: A number that specifies how small a value in the matrix has to be considered 0
    :return: The solution to the given system of linear equations
    """
    if num_of_rows is None:
        num_of_rows = len(matrix)

    num_of_cols = len(matrix[0])

    matrix = transformer(matrix, num_of_rows)
    solution = [0] * num_of_rows

    # Calculate rank of the matrix
    rank = 0
    for row in matrix:
        for value in row:
            if value != 0:
                rank += 1
                break

    if rank > num_of_cols - 1:
        raise AlgorithmError('The system of linear equations is inconsistent')
    elif rank != num_of_cols - 1 or num_of_cols == 1:
        raise AlgorithmError('The system of linear equations is dependent')

    for i in range(num_of_rows - 1, -1, -1):
        s = matrix[i][num_of_rows]
        for j in range(num_of_rows - 1, i, -1):
            s -= (matrix[i][j] * solution[j])
        if abs(matrix[i][i]) < epsilon:
            raise AlgorithmError('The system of linear equations is inconsistent')
        solution[i] = s / matrix[i][i]

    return solution
