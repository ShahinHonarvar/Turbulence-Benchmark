def all_neg_ints_exclusive(nums):
    negative = [x for x in range(20, 35) if x in nums and nums[x] < 0]
    return negative
