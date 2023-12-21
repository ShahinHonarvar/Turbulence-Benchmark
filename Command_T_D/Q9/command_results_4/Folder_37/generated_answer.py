def all_odd_ints_inclusive(nums):
    odds = [i for i in range(1, min(len(nums), 5) + 1) if nums[i] % 2 == 0]
    return [nums[i] for i in odds if i <= len(nums) - 1]
