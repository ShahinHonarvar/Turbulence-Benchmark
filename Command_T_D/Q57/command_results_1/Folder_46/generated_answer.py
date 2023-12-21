import numpy as np
def submatrix_with_particular_sum(A):
    return [s for s in np.where(np.sum(A, axis=0) == 416)[0] if np.sum(s) == 416]
