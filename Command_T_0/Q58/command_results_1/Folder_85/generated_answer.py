import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:i+13] == np.full(13, matrix[i]), axis=1) for i in range(len(matrix)-12))
