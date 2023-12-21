import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.logical_and(np.all(matrix[i:j] == matrix[i:j+1] == matrix[i:j+2] == matrix[i:j+3] == matrix[i:j+4] == matrix[i:j+5] == matrix[i:j+6] == matrix[i:j+7], i), j == len(matrix)-1))
