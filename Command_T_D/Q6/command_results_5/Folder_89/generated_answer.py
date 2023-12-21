def all_neg_ints_exclusive(nums):
    return [i for i in range(51, 77) if i in nums and nums[i] < 0]
