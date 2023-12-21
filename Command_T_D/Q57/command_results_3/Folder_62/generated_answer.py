import numpy as np
def submatrix_with_particular_sum(mat):
    mat = np.array(mat)
    return [list(x) for x in np.where(np.sum(mat, axis=1) == 394)]
