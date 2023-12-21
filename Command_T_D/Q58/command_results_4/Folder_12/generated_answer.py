import numpy as np
def submatrix_with_n_numbers(np_matrix):
    return np.sum(np.where(np_matrix.sum(axis=1) == 46)[0] != np.array([0,0,0,0]))
