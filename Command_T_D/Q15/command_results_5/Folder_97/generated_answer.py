def sum_odd_ints_inclusive(lst):
    return sum(x for x in lst[40:80:2] if x % 2 == 1)
