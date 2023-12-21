import sys
def all_pos_ints_inclusive(nums):
    result = []
    for i in range(len(nums)):
        if 31 <= i <= 34:
            result.append(nums[i])
    return result
