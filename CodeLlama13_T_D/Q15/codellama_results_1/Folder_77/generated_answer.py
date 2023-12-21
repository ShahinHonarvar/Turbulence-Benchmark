
def sum_odd_ints_inclusive(lst):
    odds = []
    for i in range(527, 539):
        if lst[i] % 2 == 1:
            odds.append(lst[i])
    return sum(odds)
