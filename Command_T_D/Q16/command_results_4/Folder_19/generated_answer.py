def sum_even_ints_inclusive(ints):
    return sum(x for x in ints[3:-2] if x % 2 == 0)
