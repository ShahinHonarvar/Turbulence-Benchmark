import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:i+83] == np.full(83, matrix[i]), axis=1) for i in range(len(matrix) - 82))
