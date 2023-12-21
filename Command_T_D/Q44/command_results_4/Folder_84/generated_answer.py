import numpy as np
def composite_nums_between_indices(nums):
    res = np.where(np.array(nums)[30:48] % np.array(nums)[0] != 0)[0]
    return set(res)
