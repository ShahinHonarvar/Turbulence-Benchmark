def all_neg_ints_inclusive(nums):
    neg_ints = [x for x in range(1, len(nums) + 1) if nums[x - 1] < 0]
    return neg_ints
