import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(matrix[i:j+122] == np.full(122, 122), axis=1) for i in range(0, len(matrix)-122) for j in range(i, len(matrix)-122))
