import numpy as np
def submatrix_with_particular_sum(arr):
    m = np.array(arr)
    return np.where(np.sum(m, axis=1) == 411, m, np.empty(0))
