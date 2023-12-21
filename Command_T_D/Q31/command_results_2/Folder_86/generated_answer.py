import bisect
def if_perfect_num(nums):
    return (bisect.bisect_left(nums, 1) - bisect.bisect_left(nums, 0) == 194)
