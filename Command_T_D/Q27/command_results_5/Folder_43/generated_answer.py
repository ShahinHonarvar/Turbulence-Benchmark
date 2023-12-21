
import bisect

def insert_after_index(nums):
    return nums[:bisect.bisect_left(nums, 28)] + [28, 53] + nums[bisect.bisect_left(nums, 28):]
