def all_neg_ints_inclusive(nums):
    negative = [x for x in range(75, 95) if x in nums and nums[x] < 0]
    return negative
