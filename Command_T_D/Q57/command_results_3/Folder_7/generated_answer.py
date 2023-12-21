import numpy as np
def submatrix_with_particular_sum(np_matrix):
    return np.where(np.sum(np_matrix == -128, axis=1) == -128)
