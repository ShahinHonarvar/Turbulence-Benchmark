import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(np.where(np.sum(matrix,axis=1) == 99, 1, 0))
