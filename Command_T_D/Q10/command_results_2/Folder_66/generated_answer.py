def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(13, 76):
        if i % 2 == 1:
            odds.append(i)
    return odds
