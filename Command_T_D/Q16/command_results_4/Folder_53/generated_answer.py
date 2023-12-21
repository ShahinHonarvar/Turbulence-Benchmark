def sum_even_ints_inclusive(lst):
    return sum(e for e in lst[111:-1] if e % 2 == 0)
