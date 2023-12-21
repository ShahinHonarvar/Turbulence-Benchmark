import numpy as np
def submatrix_with_n_numbers(nums):
    return np.count_nonzero(np.sum(np.sum(nums == num, axis=2), axis=1) == 72)
