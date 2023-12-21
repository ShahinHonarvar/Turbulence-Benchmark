def all_neg_ints_exclusive(nums):
    return [x for x in range(len(nums)) if nums[x] < 0 and x != len(nums) - 1]
