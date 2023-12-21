def sum_odd_ints_inclusive(lst):
    return sum(n for n in range(40, 80+1, 2) if n in lst)
