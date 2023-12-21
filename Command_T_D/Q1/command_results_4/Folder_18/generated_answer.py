
def all_ints_inclusive(nums):
    return list(range(min(nums[28:], default=-1), max(nums[28:], default=len(nums)-1) + 1))
