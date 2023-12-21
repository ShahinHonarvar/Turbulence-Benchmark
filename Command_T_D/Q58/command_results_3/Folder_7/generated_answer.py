import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for row in range(len(matrix)) if all(x == matrix[row][i] for i, x in enumerate(row)))
