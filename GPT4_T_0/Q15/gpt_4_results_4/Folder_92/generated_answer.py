
def sum_odd_ints_inclusive(lst):
    return sum(i for i in lst[1:2] if i % 2 != 0)
