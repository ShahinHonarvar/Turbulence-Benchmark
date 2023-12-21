def all_neg_ints_inclusive(nums):
    return list(range(len(nums) + 1) for i in range(len(nums)) if nums[i] < 0)
