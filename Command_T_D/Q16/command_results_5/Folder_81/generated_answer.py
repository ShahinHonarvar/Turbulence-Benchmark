def sum_even_ints_inclusive(lst):
    return sum(i for i in range(10, 100, 2) if i in lst)
