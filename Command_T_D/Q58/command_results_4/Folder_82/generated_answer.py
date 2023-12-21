import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(np.sum(nums,axis=1) == 99,axis=0)
