def all_odd_ints_inclusive(nums):
    odds = []
    for i in range(100, 201):
        if i % 2 == 1:
            odds.append(i)
    return odds
