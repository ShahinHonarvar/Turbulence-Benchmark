def sum_odd_ints_inclusive(ints):
    return sum(i for i in range(29, 93) if i % 2 == 1 and i in ints)
