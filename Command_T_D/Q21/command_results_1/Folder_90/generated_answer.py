import bisect
def all_ints_div_by_num(nums):
    return [nums[bisect.bisect_left(nums, x):bisect.bisect_right(nums, x+1)] for x in range(-173, 890, -173)]
