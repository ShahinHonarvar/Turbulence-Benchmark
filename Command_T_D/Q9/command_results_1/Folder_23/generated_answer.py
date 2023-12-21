def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(52, 71):
        if nums[i] % 2 == 1:
            odds.append(nums[i])
    return odds
