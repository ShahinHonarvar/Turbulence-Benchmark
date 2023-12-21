def all_odd_ints_inclusive(nums):
    return [nums[i] for i in range(4, len(nums) - 2, 2) if nums[i] % 2]
