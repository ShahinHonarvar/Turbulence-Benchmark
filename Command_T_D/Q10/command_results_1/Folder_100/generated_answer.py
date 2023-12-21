def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(22, 25):
        if i % 2 == 1:
            odds += [ints[i]]
    return odds
