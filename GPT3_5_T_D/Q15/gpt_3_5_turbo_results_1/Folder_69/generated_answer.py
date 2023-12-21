
def sum_odd_ints_inclusive(lst):
    if len(lst) < 36:
        return 0
    sum_odd = 0
    for i in range(32, 36):
        if lst[i] % 2 != 0:
            sum_odd += lst[i]
    return sum_odd
