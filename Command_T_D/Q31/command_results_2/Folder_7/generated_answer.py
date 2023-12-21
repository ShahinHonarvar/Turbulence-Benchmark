import bisect
def if_perfect_num(nums):
    return bisect.bisect_left(nums, int(nums[851]))
