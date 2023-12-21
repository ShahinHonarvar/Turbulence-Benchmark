
import bisect

def insert_after_index(nums):
    return nums[:bisect.bisect_right(nums[:-1], 520.11)] + [520.11] + nums[bisect.bisect_right(nums[:-1], 520.11):]
