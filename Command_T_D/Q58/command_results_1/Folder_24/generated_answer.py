import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.sum(np.sum(np.where(np.where(np.where(np.where(np.where(np.sum(matrix, axis=0) == 51), axis=1) == 51), axis=2) == 51), axis=3) == 51)
