import numpy as np
def submatrix_with_n_numbers(nums):
    if not isinstance(nums, np.ndarray):
        return 0
    return np.sum(np.array(range(0,len(nums),41), dtype=np.int32) == np.sum(nums,axis=1))
