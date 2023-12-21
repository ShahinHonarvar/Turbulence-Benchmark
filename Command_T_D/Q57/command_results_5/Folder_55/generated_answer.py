import numpy as np
def submatrix_with_particular_sum(np_matrix):
    return np.where(np_matrix.sum(axis=1).sum(axis=1) == 1)
