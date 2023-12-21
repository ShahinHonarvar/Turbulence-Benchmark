import numpy as np
def composite_nums_between_indices(nums):
    return set(np.where(np.all(np.array(range(2, nums[6]+1)) % nums == 0, axis=1), True, False)[0].tolist())
