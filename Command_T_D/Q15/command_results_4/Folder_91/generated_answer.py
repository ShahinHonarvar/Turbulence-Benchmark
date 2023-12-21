def sum_odd_ints_inclusive(ints):
    return sum(x for x in range(ints[0], ints[5] + 1) if x % 2)
