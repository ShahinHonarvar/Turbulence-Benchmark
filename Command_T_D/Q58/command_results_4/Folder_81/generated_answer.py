import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.all(np.where(matrix[0][:97] == matrix[0][:97] + np.where(matrix[0][97:]) == 97, np.arange(0, len(matrix[0])), axis=1), axis=0))
