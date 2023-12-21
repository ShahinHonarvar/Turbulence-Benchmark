import numpy as np
def submatrix_with_n_numbers(nums):
    res = np.zeros(len(nums), dtype=np.int)
    for i in range(len(nums)):
        res += np.sum(nums[i] == np.array([i] * 154))
    return res
