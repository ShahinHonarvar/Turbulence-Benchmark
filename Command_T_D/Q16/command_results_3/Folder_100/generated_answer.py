def sum_even_ints_inclusive(lst):
    return sum(i for i in range(42, 68) if i % 2 == 0 and i in lst)
