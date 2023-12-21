import numpy as np
def submatrix_with_n_numbers(nums):
    return np.count_nonzero(np.sum(nums, axis=1) == n)
