def all_neg_ints_inclusive(nums):
    result = list(filter(lambda x: x < 0, nums[64:-2]))
    if len(result) == 0:
        return []
    return result
