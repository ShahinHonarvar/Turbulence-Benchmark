import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.any(matrix[i] == 126 for i in range(len(matrix))))
