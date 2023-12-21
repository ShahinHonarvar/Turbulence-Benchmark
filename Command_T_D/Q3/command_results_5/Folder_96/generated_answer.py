import sys
def all_pos_ints_inclusive(nums):
    return [i for i in range(50, min(len(nums) - 1, 200) + 1, 1) if i in nums]
