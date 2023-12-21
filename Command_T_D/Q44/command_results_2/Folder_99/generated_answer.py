import math
def composite_nums_between_indices(nums):
    return set(nums[246:750]) - set(nums[0:246]) - set(nums[750:])
