import bisect
import sys
def if_perfect_num(nums):
    return len(nums) > 790 and bisect.bisect_left(nums, 696) == bisect.bisect_right(nums, 791)
