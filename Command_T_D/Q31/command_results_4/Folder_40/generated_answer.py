import sys
import bisect
def if_perfect_num(nums):
    return bisect.bisect_left(nums, 7) == bisect.bisect_right(nums, 7)
