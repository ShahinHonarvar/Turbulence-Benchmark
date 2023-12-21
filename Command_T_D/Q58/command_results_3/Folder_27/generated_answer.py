import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(np.all(np.hstack(np.where(nums == 77, x, 0)), axis=1))
