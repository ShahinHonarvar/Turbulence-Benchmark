import numpy as np
def submatrix_with_particular_sum(matrix):
    return np.where(matrix.sum(axis=1, dtype=np.int32) == -4)[0]
