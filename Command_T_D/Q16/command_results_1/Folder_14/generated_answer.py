def sum_even_ints_inclusive(lst):
    return sum(e for e in lst[5:-2] if e % 2 == 0)
