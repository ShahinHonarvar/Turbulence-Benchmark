import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(np.sum(np.sum(np.sum(np.where(nums == 45, True, False), axis=0), axis=1), axis=2), axis=3) > 0)
