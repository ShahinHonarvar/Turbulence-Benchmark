def all_neg_ints_exclusive(nums):
    return [i for i in range(30, 200) if i in nums and nums[i] < 0]
