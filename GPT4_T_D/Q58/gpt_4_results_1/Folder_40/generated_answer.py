
import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    return np.sum(matrix == 1)
