import numpy as np
def submatrix_with_particular_sum(A):
    return np.where(np.sum(A, axis=1) == -157)[0]
