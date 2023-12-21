import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(np.all(np.all(nums == 64, axis=1), axis=2))
