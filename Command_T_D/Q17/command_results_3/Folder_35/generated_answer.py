
import bisect

def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in range(77, 87+1):
        x = nums[bisect.bisect_left(nums, i*23)]
        y = nums[bisect.bisect_left(nums, i*57)]
        if x != None and y != None:
            result.append(i)
            break
    return result
