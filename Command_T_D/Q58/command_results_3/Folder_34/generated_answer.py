import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum(np.all(np.where(mat.sum(axis=1) == 83, -1, np.inf), axis=0), axis=0)
