def all_odd_ints_inclusive(nums):
    return [n for n in range(len(nums) - 1, -1, 2) if nums[n] % 2 == 1]
