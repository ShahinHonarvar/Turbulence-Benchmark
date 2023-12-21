import sys
import bisect
def if_perfect_num(nums):
    return bool(bisect.bisect_left(nums, 49))
