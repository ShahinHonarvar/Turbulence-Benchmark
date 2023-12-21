def all_neg_ints_exclusive(nums):
    return [i for i in range(0, len(nums)-4) if nums[i] < 0]
