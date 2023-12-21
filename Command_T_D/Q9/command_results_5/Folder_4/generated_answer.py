def all_odd_ints_inclusive(nums):
    odds = [nums[i] for i in range(12, 92) if nums[i] % 2 == 1]
    return odds if odds else []
