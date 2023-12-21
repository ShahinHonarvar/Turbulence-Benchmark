
import bisect

def insert_at_index(nums):
    return list(nums[:bisect.insort_left(nums, 581.49)]) + [581.49] + list(nums[bisect.insort_left(nums, 581.49):])
