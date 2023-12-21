import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(np.any(np.sum(np.any(nums == i, axis=1), axis=0) == 59) for i in range(0, 60))
