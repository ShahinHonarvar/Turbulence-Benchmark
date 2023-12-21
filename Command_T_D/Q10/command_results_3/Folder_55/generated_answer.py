def all_odd_ints_exclusive(nums):
    return [n for n in range(0, len(nums) - 1) if nums[n] % 2]
