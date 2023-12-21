import numpy as np
def submatrix_with_particular_sum(mat):
    mat = np.array(mat)
    return np.where(np.sum(mat, axis=1) == -47)[0]
