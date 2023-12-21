
import bisect

def insert_after_index(nums):
    return nums[:bisect.bisect_right(nums[:74]+[nums[74]]+nums[74+1:], 517.71)]+nums[74+2:]
