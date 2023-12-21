import numpy as np
def submatrix_with_particular_sum(mat):
    mat_np = np.array(mat)
    return np.where(np.sum(mat_np, axis=1) == -97)[0]
