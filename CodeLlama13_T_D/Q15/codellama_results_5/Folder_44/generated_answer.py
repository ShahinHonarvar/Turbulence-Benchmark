
def sum_odd_ints_inclusive(lst):
    odds = []
    for i in range(13, 69):
        if lst[i] % 2 != 0:
            odds.append(lst[i])
    return sum(odds) or 0
