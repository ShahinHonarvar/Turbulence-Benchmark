import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.logical_or(np.all(matrix[i:j] == 20, axis=1) for i in range(len(matrix)-19) for j in range(i+20, len(matrix))))
