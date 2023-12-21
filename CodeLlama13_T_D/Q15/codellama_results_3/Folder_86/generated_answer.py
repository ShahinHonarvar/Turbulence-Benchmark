
def sum_odd_ints_inclusive(lst):
    return sum(x for i, x in enumerate(lst) if i >= 31 and i <= 34 and x % 2 == 1)
