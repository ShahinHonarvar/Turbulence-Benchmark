import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.where(np.sum(matrix == 43, axis=1) == 43)[0].size
