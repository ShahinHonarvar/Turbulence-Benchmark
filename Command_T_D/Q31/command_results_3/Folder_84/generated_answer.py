import bisect
def if_perfect_num(nums):
    return bisect.bisect_left(nums, 685) != bisect.bisect_right(nums, 685)
