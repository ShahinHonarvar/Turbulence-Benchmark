
import bisect

def insert_after_index(nums):
    return nums[:500] + [912, 170] + bisect.insort_right(nums[500+1:], [912, 170])
