def all_neg_ints_exclusive(nums):
    return [i for i in range(len(nums) - 2, len(nums) - 5, -1) if nums[i] < 0]
