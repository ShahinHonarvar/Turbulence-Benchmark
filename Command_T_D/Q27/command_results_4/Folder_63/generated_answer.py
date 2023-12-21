
import bisect

def insert_after_index(nums):
    idx = bisect.bisect_right(nums, [15, 51])
    nums.insert(idx, [15, 51])
    return nums
