def sum_odd_ints_inclusive(lst):
    return sum(x for x in lst[50:-1] if x % 2)
