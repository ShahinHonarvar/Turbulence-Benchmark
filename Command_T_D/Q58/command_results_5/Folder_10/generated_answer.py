import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(np.all(matrix == num, axis=2), axis=1) for num in range(0, 57))
