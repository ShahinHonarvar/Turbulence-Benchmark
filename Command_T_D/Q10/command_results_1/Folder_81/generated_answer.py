def all_odd_ints_exclusive(nums):
    return [n for n in range(10, len(nums) + 1, 2) if n in nums]
