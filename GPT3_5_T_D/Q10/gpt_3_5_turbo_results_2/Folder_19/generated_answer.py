
def all_odd_ints_exclusive(lst):
    odds = []
    for i in range(2, 5):
        if lst[i] % 2 != 0:
            odds.append(lst[i])
    return odds
