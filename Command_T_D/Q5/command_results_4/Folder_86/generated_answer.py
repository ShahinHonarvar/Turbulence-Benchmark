def all_neg_ints_inclusive(nums):
    result = [x for x in range(31, 35) if x in nums and nums[x] < 0]
    return result
