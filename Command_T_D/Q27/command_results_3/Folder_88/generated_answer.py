
import bisect

def insert_after_index(nums):
    return nums[:bisect.bisect_right(nums, [46, 13])] + [91] + nums[bisect.bisect_right(nums, [46, 13]):] + nums[bisect.bisect_right(nums, [46, 13]):]
