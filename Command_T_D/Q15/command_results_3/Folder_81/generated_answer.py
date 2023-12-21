def sum_odd_ints_inclusive(lst):
    return sum(x for x in lst[10:100:2] if x % 2 == 1)
