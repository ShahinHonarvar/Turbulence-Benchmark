import numpy as np
def submatrix_with_particular_sum(mat):
    mat = np.array(mat)
    return np.where(np.all(mat == -863, axis=1))[0]
