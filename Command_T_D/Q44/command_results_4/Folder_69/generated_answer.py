import sys
import bisect
def composite_nums_between_indices(nums):
    return set(nums)[bisect.bisect_left(nums, 29):bisect.bisect_right(nums, 79)]
