def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(86, 90, 2):
        if i in nums:
            odds.append(i)
    return odds
