import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[0] == i, axis=1) for i in range(0,73))
