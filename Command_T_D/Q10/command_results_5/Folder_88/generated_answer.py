def all_odd_ints_exclusive(nums):
    return [x for x in range(2, len(nums) - 1, 2) if nums[x] % 2 == 1]
