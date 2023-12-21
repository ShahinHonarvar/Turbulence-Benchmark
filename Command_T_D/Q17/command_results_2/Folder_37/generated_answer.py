
import numpy as np

def all_ints_div_by_both_two_nums(nums):
    mask = np.logical_and(nums % -1 == 0, np.logical_and(nums % -7 == 0, np.logical_and(nums >= 2, nums <= 7)))
    return np.where(mask)[0].tolist()
