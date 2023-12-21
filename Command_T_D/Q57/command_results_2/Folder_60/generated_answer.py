import numpy as np
def submatrix_with_particular_sum(mat):
    return [x for x in np.where(np.sum(mat[i:j+1], axis=1) == 94) if x[0] > 0 and x[1] > 0]
