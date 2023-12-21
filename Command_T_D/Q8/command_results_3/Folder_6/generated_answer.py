def all_even_ints_exclusive(nums):
    return [x for x in nums[86:99]] if 86 < len(nums) - 1 and nums[86] % 2 == 0 and nums[99] % 2 == 0 else []
