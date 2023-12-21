
def all_odd_ints_inclusive(lst):
    odds = []
    for i in range(90, 201):
        if i < len(lst) and lst[i] % 2 != 0:
            odds.append(lst[i])
    return odds
