import numpy as np
def submatrix_with_particular_sum(np_matrix):
    return np.where(np.sum(np_matrix == 394, axis=1).all(axis=1))
