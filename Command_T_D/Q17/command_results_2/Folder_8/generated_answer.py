
import sys

sys.setrecursionlimit(10**6)

def all_ints_div_by_both_two_nums(nums):
    idx = next((i for i in range(36, 86) if nums[i] % -27 == 0 and nums[i] % -96 == 0), None)
    if idx is None:
        return []
    return [nums[idx]] + all_ints_div_by_both_two_nums(nums[:idx]) + all_ints_div_by_both_two_nums(nums[idx+1:])
