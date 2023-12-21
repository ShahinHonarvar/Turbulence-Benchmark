def sum_even_ints_inclusive(ints):
    return sum(i for i in range(3, len(ints) - 1, 2) if i % 2 == 0)
