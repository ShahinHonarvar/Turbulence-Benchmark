
def all_odd_ints_exclusive(list):
    odds = []
    for i in range(51, 76):
        if list[i] % 2 == 1:
            odds.append(list[i])
    return odds
