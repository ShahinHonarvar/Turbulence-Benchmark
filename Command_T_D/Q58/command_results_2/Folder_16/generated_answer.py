import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(np.where(nums == np.array([i * 154 for i in range(nums.shape[0])]), True, False))
