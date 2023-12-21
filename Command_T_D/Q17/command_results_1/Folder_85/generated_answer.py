
import numpy as np

def all_ints_div_by_both_two_nums(nums):
    return np.where(np.logical_and(nums % -9 == 0, nums % -3 == 0), range(1, 9), np.array([])).tolist()
