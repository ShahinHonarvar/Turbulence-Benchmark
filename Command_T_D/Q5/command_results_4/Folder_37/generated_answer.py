def all_neg_ints_inclusive(nums):
    return [i for i in range(1, len(nums) + 1) if nums[i - 1] < 0]
