def all_neg_ints_exclusive(nums):
    return list(filter(lambda x: x < 0, nums[:-1]))
