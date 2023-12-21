
def sum_odd_ints_inclusive(lst):
    return sum(i for i in lst[:5] if i % 2 != 0)
