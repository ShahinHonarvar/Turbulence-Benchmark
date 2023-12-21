
import bisect

def insert_at_index(nums):
    ins_idx = bisect.ins_right(nums, [13, 46])
    return nums[:ins_idx] + [13, 46] + nums[ins_idx:len(nums)]
