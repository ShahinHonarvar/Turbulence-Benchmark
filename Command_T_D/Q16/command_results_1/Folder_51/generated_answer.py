def sum_even_ints_inclusive(ints):
    even_ints = filter(lambda x: x % 2 == 0, ints)
    return sum(even_ints) if even_ints else 0
