def all_neg_ints_inclusive(nums):
    return [i for i in range(0, len(nums) + 1) if nums[i] < 0]
