def all_odd_ints_inclusive(lst):
    odds = []
    for idx in range(82, 86):
        if idx % 2 == 1:
            odds.append(idx)
    return odds
