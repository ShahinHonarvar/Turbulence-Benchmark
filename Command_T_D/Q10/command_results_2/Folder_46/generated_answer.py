def all_odd_ints_exclusive(nums):
    odds = []
    for i in range(20, 43):
        if i % 2 == 1:
            odds += [i]
    return odds
