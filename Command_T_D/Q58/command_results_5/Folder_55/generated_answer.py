import numpy as np
def submatrix_with_n_numbers(arr):
    matrix = np.array(arr)
    return np.sum(np.sum(matrix, axis=1) == 39)
