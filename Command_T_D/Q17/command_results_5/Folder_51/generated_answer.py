
import numpy as np

def all_ints_div_by_both_two_nums(nums):
    if not nums:
        return np.array([])
    return np.where(np.logical_and(nums[6:8] % -1 == 0, nums[6:9] % -10 == 0))[0]
