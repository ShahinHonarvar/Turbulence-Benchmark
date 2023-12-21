def sum_odd_ints_inclusive(ints):
    return sum(i for i in range(59, 97, 2) if i in ints)
