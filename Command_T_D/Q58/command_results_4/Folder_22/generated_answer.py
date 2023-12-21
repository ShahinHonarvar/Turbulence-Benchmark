import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(np.all(np.sum(nums, axis=0) == 21, axis=1))
