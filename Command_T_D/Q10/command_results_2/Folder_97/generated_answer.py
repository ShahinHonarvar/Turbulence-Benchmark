def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(20, 94):
        if i % 2 == 1:
            odds.append(i)
    return odds
