def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(28, 32):
        if i % 2 == 1:
            odds.append(nums[i])
    return odds
