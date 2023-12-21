def sum_even_ints_inclusive(lst):
    return sum(x for x in lst[6:-1] if x % 2 == 0)
