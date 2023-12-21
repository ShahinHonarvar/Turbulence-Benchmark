def sum_odd_ints_inclusive(lst):
    return sum(x for x in lst[30:200] if x % 2 == 1)
