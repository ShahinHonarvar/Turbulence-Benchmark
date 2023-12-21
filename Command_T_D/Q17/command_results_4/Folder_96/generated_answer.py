
import bisect

def all_ints_div_by_both_two_nums(nums):
    lst = []
    for i in range(50, 200):
        if nums[i] % 64 == 0 and nums[i] % -34 == 0:
            lst.append(nums[i])
    return lst
