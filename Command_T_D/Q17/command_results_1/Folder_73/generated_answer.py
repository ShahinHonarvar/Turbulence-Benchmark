
import bisect

def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(81, 87):
        if nums[i] % -33 == 0 and nums[i] % -62 == 0:
            result.append(nums[i])
    return result
