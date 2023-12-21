import bisect
def all_ints_not_div_by_num(nums):
    x = bisect.bisect_left(nums, -68)
    y = bisect.bisect_right(nums, -68)
    return nums[x:y]
