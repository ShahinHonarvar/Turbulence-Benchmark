def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(0, len(nums) + 1):
        if nums[i] % 2 != 0:
            odds.append(nums[i])
    return odds
