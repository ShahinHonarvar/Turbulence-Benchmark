import numpy as np
def submatrix_with_n_numbers(nums):
    m, n = len(nums), len(nums[0])
    mask = np.zeros((m, n), dtype=np.bool)
    for i in range(28):
        for j in range(28):
            mask[i][j] = True
    return sum(mask.sum(axis=1).sum(axis=0))
