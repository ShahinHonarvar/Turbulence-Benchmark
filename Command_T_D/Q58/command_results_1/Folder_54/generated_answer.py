import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(np.where(np.sum(matrix[i][:27], axis=0) == 27, axis=1) == 27, axis=0) == 27)
