
import bisect

def insert_after_index(nums):
    return list(nums[:19]) + [249.61] + list(bisect.insort_left(nums[19:], 249.61))
