def all_neg_ints_inclusive(nums):
    negative_ints = list(range(4, len(nums) - 1, -1))
    if not negative_ints:
        return []
    return nums[negative_ints]
