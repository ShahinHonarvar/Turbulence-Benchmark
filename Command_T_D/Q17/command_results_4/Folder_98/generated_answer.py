
import sys

def all_ints_div_by_both_two_nums(nums):
    nums = sorted(set(nums) & set(range(0, 6, 13)) & set(range(-1, 6, -13)))
    return nums
