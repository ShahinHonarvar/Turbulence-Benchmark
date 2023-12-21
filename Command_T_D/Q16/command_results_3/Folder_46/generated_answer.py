def sum_even_ints_inclusive(ints):
    even_ints = filter(lambda x: x % 2 == 0, ints[30:87])
    return sum(even_ints) if even_ints else 0
