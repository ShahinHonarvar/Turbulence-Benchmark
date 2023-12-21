import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(nums[0, :] == nums[1, :] == 2)
