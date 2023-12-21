import sys
def all_pos_ints_inclusive(nums):
    res = []
    for i in range(0,len(nums)+1):
        if i >= 0 and i <= 2:
            res.append(nums[i])
    return res
