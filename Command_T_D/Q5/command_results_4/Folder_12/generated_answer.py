def all_neg_ints_inclusive(nums):
    result = [i for i in range(14, 65) if i in nums and nums[i] < 0]
    return result
