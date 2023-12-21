
def all_odd_ints_inclusive(lst):
    odds = []
    for i in range(62, 79):
        if lst[i] % 2 != 0:
            odds.append(lst[i])
    return odds
