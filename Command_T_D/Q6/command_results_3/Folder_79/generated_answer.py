def all_neg_ints_exclusive(nums):
    return [i for i in range(3, len(nums) - 1, -1) if nums[i] < 0]
