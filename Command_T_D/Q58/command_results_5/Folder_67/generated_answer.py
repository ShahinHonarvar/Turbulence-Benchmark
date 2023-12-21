import numpy as np
def submatrix_with_n_numbers(arr):
    matrix = np.matrix(arr)
    return sum(matrix.shape[0] - row < 43 for row in range(matrix.shape[0]))
