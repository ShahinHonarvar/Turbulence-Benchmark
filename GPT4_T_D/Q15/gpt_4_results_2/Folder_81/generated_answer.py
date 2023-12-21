
def sum_odd_ints_inclusive(lst):
    sublist = lst[10:101]
    sum_odd = sum(i for i in sublist if i % 2 != 0)
    return sum_odd
