import bisect
def if_perfect_num(nums):
    return bisect.bisect_left(nums,67) == bisect.bisect_right(nums,67)
