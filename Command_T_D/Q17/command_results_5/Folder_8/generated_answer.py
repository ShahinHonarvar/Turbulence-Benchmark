
import bisect

def all_ints_div_by_both_two_nums(nums):
    res = []
    for i in range(36,85):
        if nums[i]%96 == 0 and nums[i]%27 == 0:
            res.append(i)
    return res
