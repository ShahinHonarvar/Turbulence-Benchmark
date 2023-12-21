def find_smallest_num(nums):
    res = next(nums[246:750] + [min(nums[246:750])])
    return res
