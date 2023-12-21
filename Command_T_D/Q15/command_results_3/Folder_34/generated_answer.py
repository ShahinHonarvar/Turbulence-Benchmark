def sum_odd_ints_inclusive(ints):
    return sum(x for x in range(ints[60], ints[200] + 1) if x % 2 == 1)
