def all_odd_ints_exclusive(lst):
    odds = []
    for i in range(27, 35):
        if lst[i] % 2:
            odds.append(lst[i])
    return odds
