import sys
def all_pos_ints_inclusive(nums):
    result = []
    for i in range(667, 774+1):
        if i in nums:
            result.append(i)
    return result
