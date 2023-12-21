import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(
        np.all(matrix[row][:78] == np.full(78, row), axis=1)
        for row in range(len(matrix))
    )
