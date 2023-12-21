def all_neg_ints_exclusive(nums):
    return nums[nums.index(min(nums)) : nums.index(max(nums)) + 1]
