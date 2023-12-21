import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:i+84] == np.full(84, matrix[i]), axis=1) for i in range(len(matrix) - 83))
