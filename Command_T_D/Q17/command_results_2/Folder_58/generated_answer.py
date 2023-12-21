
import bisect

def all_ints_div_by_both_two_nums(nums):
    res = []
    for i in range(240, 901):
        if nums[i] % 546 == 0 and nums[i] % 709 == 0:
            res.append(nums[i])
    return res
