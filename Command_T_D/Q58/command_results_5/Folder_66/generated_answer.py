import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return np.sum(np.all(matrix == 42, axis=1))
