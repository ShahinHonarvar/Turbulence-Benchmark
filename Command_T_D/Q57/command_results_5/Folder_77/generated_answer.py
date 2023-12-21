import numpy as np
def submatrix_with_particular_sum(mat):
    return [sub for row in range(len(mat)) for sub in np.where(np.sum(mat[row], axis=1) == -336)]
