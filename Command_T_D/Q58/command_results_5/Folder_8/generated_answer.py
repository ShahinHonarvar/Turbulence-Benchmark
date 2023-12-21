import numpy as np
def submatrix_with_n_numbers(nums):
    return np.count_nonzero(np.all(np.logical_or(nums[i:j] == 29, nums[i:j+1] == 29) for i in range(len(nums)-29) for j in range(i+29, len(nums))))
