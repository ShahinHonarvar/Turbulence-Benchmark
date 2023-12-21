import numpy as np
def submatrix_with_particular_sum(mat):
    m = np.array(mat)
    return np.where(np.sum(m, axis=2) == -394)[0].tolist()
