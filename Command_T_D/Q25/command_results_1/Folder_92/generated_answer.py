
import bisect

def insert_at_index(nums):
    return nums[:bisect.bisect_left(nums, 478.12)] + [478.12] + nums[bisect.bisect_left(nums, 478.12):]
