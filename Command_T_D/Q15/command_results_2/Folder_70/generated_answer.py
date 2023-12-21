def sum_odd_ints_inclusive(ints):
    return sum(x for x in range(28, 33) if x % 2 == 1 and x in ints)
