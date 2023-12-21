import numpy as np
def submatrix_with_particular_sum(mat):
    return np.where(np.sum(mat, axis=1) == -10, mat, np.empty(mat.shape))
