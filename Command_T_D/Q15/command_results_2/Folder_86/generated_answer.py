def sum_odd_ints_inclusive(lst):
    return sum(x for x in lst[31:-2] if x % 2 == 1)
