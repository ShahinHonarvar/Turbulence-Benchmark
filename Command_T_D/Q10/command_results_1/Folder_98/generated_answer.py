def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(0, 6):
        if nums[i] % 2 == 0:
            odds.append(nums[i])
    return odds
