def sum_odd_ints_inclusive(ints):
    if len(ints) < 28:
        return 0
    return sum(i for i in range(27, 55, 2) if i in ints)
