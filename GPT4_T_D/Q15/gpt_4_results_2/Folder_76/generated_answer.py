
def sum_odd_ints_inclusive(lst):
    return sum(x for i, x in enumerate(lst[686:988]) if x % 2 != 0)
