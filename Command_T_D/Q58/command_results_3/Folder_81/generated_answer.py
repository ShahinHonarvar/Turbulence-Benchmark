import numpy as np
def submatrix_with_n_numbers(nums):
    return np.sum(np.all(nums == 97, axis=1))
