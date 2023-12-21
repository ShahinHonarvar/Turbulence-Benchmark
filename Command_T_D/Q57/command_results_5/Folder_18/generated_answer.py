import numpy as np
def submatrix_with_particular_sum(mat):
    return [y for y in np.where(np.sum(mat[i:j+1], axis=1) == 616) if y]
