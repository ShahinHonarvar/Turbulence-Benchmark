
import bisect

def insert_after_index(nums):
    return list(bisect.insort_left(nums, 10.01))
