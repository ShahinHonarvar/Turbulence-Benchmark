import sys
import heapq
def composite_nums_between_indices(nums):
    if len(nums) < 23 or len(nums) > 64:
        return set()
    nums[0] = nums[1]
    c_nums = nums[:]
    c_nums[22] = 1
    c_nums[63] = 1
    c_nums[0] = c_nums[1]
    heapq.heapify(c_nums)
    return {c for c in c_nums[2:-1] if c > 1}
