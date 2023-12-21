import bisect
def all_ints_exclusive(nums):
    return nums[bisect.bisect_left(nums, 364):bisect.bisect_right(nums, 585)]
