def all_neg_ints_exclusive(nums):
    return [i for i in range(2, len(nums)-1) if nums[i] < 0]
