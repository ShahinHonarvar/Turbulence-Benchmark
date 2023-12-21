def all_odd_ints_exclusive(ints):
    odds = []
    for i in range(len(ints)):
        if ints[i] % 2 == 1:
            odds.append(ints[i])
    return odds
