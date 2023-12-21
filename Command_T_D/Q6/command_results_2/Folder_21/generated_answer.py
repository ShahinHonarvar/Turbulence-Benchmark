def all_neg_ints_exclusive(nums):
    return nums[743:867] if 743 in nums and 867 in nums and all(x < 0 for x in nums[743:867]) else []
