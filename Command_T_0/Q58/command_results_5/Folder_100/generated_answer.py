import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i:i+10] == np.full(10, True), axis=1) for i in range(0, len(matrix)-9))
