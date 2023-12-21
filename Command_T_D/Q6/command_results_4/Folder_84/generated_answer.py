def all_neg_ints_exclusive(nums):
    result = [i for i in range(50, 93) if i in nums and nums[i] < 0]
    return result
