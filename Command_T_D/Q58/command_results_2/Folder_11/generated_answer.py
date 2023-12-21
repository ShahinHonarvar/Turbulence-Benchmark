import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(np.all(nums == nums[i:j+1] for i in range(len(nums)-37) for j in range(i+1,len(nums)+1)))
