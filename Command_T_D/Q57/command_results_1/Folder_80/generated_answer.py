import numpy as np
def submatrix_with_particular_sum(A):
    return [list(z) for z in np.where(A.sum(axis=1) == 245)[0]]
