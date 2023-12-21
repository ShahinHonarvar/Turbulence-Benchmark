def all_odd_ints_exclusive(nums):
    odds = [i for i in range(2, len(nums) + 1, 2) if nums[i - 2] % 2 == 1]
    return [nums[o - 2] for o in odds if o < 5]
