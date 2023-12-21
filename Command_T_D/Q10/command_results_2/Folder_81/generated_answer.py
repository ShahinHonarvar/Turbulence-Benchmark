def all_odd_ints_exclusive(nums):
    return [x for x in range(10, nums[10] + 1, 2) if x in nums]
