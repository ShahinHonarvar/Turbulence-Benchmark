
import bisect

def insert_after_index(nums):
    return nums[:21] + [74] + bisect.insort_right(nums[21:], 74)
