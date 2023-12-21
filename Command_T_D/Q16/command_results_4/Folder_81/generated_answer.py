def sum_even_ints_inclusive(ints):
    return sum(i for i in range(10, 100, 2) if i in ints)
