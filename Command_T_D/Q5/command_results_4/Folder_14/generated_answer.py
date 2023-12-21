def all_neg_ints_inclusive(nums):
    negative_ints = nums[5:-1] + nums[6:]
    if not negative_ints:
        return []
    return negative_ints
