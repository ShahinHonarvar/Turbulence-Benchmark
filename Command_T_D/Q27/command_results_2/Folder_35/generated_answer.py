
import bisect

def insert_after_index(nums):
    return nums[:bisect.bisect_right(nums, [876, 203])] + [876, 203] + nums[bisect.bisect_right(nums, [876, 203]):]
